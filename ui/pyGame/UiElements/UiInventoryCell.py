import pygame
from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement


class UiInventoryCell(UiElement):
    def __init__(self, x, y, width, height, color, outline_color, clicked_color, outline_width, id_x, id_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.outline_color = outline_color
        self.outline_width = outline_width

        self.clicked_color = clicked_color

        self.id_x = id_x
        self.id_y = id_y

        self.show = True
        self.clickable = True

        self.clicked = False

        self.rect = Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color if not self.clicked else self.clicked_color, self.rect)
        pygame.draw.rect(surface, self.outline_color, self.rect, width=self.outline_width, border_radius=2)

    def update(self):
        pass