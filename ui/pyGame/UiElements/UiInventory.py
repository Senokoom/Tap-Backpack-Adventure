from PIL.DdsImagePlugin import item

from classes.AppController import AppController
from ui.pyGame.Scenes.MainScene import MainScene
from ui.pyGame.UiElements.UiElement import UiElement
from ui.pyGame.UiElements.UiInventoryCell import UiInventoryCell
import pygame
from pygame import Rect

class UiInventory(UiElement):
    def __init__(self, name,x, y, controller: AppController,inventory_dict, inventory_width_height, item_color_mapping, cell_width, cell_height, cell_default_color, cell_outline_color, clicked_color, cell_outline_width):
        self.name = name

        self.x = x
        self.y = y

        self.controller = controller

        inventory_width, inventory_height = inventory_width_height

        self.width = cell_width * inventory_width
        self.height = cell_height * inventory_height

        self.inventory_dict = inventory_dict
        self.item_color_mapping = item_color_mapping
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_default_color = cell_default_color
        self.cell_outline_color = cell_outline_color
        self.cell_outline_width = cell_outline_width

        self.item_selected = None

        self.clicked_color = clicked_color

        self.rect = Rect(self.x, self.y, self.width, self.height)

        self.cell_list = [ [[] for j in range(inventory_width)] for i in range(inventory_height)]
        cell_y = self.y
        for i in range(len(inventory_dict)):
            string = ""
            cell_x = self.x
            for j in range(len(inventory_dict[i])):
                string += " " + str(inventory_dict[i][j])
                self.cell_list[i][j] = (UiInventoryCell(cell_x, cell_y, self.cell_width, self.cell_height, self.cell_default_color, self.cell_outline_color, self.clicked_color, self.cell_outline_width, j, i))
                cell_x += self.cell_width
            cell_y += self.cell_height
        self.clickable = True
        self.show = True

    def draw(self, surface):
        for cell_line in self.cell_list:
            for cell in cell_line:
                cell.draw(surface)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)

    # row.append({
    #     "name": cell.item.name,
    #     "rarity": cell.item.rarity,
    #     "stats": cell.item.current_stats
    # })

    def clicked_off(self):
        for cell_line in self.cell_list:
            for cell in cell_line:
                cell.clicked = False
        self.item_selected = None


    def execute(self, event):
        if event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for cell_line in self.cell_list:
                for cell in cell_line:
                    cell.clicked = False
                if clicked_obj := MainScene.checkIntersection(cell_line, mouse_pos):
                    clicked_obj.clicked = True
                    if self.item_selected:
                        if not self.controller.get_item_move_by_player(clicked_obj.id_y, clicked_obj.id_x, self.item_selected, self.name):
                            self.item_selected = None
                    if self.inventory_dict[clicked_obj.id_y][clicked_obj.id_x]:
                        self.item_selected = self.controller.get_item_from_inventory_by_coordinates(clicked_obj.id_x, clicked_obj.id_y, self.name)
                    print(f"Предмет по адресу [{clicked_obj.id_y}] [{clicked_obj.id_x}] {self.inventory_dict[clicked_obj.id_y][clicked_obj.id_x]}\nВыделен предмет {self.item_selected}")
                    if self.item_selected:
                        print(self.item_selected)
        if event.button == 3 and self.item_selected:
            self.controller.get_item_rotated(self.item_selected, self.name)







    def print_inventory(self):
        for i in range(len(self.inventory_dict)):
            string = ""
            for j in range(len(self.inventory_dict[i])):
                string += " " + str(self.inventory_dict[i][j])
            print(string)


    def update(self):
        self.inventory_dict = self.controller.get_inventory_ui_data(self.name)
        for cell_line in self.cell_list:
            for cell in cell_line:
                if self.inventory_dict[cell.id_y][cell.id_x]:
                    cell.color = self.item_color_mapping[self.inventory_dict[cell.id_y][cell.id_x]["rarity"]]
                else:
                    cell.color = self.cell_default_color