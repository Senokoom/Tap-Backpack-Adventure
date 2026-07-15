import pygame
import gif_pygame

from ui.pyGame.Scenes.BaseScene import BaseScene
from ui.pyGame.UiElements.UiButton import UiButton
from ui.pyGame.UiElements.UiGifBackground import UiGifBackground
from ui.pyGame.UiElements.UiAnimatedLogo import UiAnimatedLogo
from ui.pyGame.UiElements.UiLabel import UiLabel
from ui.pyGame.UiElements.UiTextBox import UiTextBox
from ui.ui_config import UiConfig

class MainScene(BaseScene):
    def __init__(self, name, controller, number):
        self.name = name
        self.controller = controller
        self.number = number

        self.ui_objects = []

        self.ui_objects.append(
            UiGifBackground(100, 0, gif_pygame.load(UiConfig.main_menu_gif_path), (800, 600)))
        self.ui_objects.append(UiAnimatedLogo(15, 20, pygame.image.load(UiConfig.logo_path)))
        self.ui_objects.append(UiButton("LoadGame", 90, 480, 180, 70, (63, 110, 30),
                                                   pygame.font.Font(UiConfig.game_font, 20), "Load Game", 0,
                                                   lambda: self.controller.load_game(),  (16, 6, 6)))
        self.ui_objects.append(
            text_box := UiTextBox(60, 300, 250, 50, (205, 205, 205), pygame.font.Font(UiConfig.game_font, 25),(16, 6, 6)))
        self.ui_objects.append(name_error_label := UiLabel(40, 270, 100, 100, pygame.font.Font(UiConfig.game_font, 15), "Enter your Hero's name", (255, 255, 255)))
        name_error_label.show = False
        self.ui_objects.append(UiButton("NewGame", 90, 380, 180, 70, (153, 90, 8),
                                                   pygame.font.Font(UiConfig.game_font, 20), "New Game", 0,
                                                   lambda: self.controller.start_new_game(
                                                       text_box.text) if text_box.text != "" else self.no_name_error(name_error_label), (16, 6, 6)))
        self.clicked_obj = None

    def no_name_error(self, label):
        label.show = True
        raise ValueError("Can't Create Hero Without A Name")

    def update(self):
        for obj in self.ui_objects:
            obj.update()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.clicked_obj and isinstance(self.clicked_obj, UiTextBox):
                self.clicked_obj.handle_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.clicked_obj = self.checkIntersection(pygame.mouse.get_pos())
            for obj in self.ui_objects:
                obj.clicked = False
            if self.clicked_obj and isinstance(self.clicked_obj, UiTextBox):
                self.clicked_obj.clicked = True
            elif self.clicked_obj and isinstance(self.clicked_obj, UiButton):
                self.clicked_obj.execute()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked_obj = self.checkIntersection(pygame.mouse.get_pos())
            if self.clicked_obj:
                self.clicked_obj.clicked = True

    def draw(self, surface):
        for obj in self.ui_objects:
            if obj.show:
                obj.draw(surface)


    def checkIntersection(self, mxy):
        m_x, m_y = mxy
        for obj in self.ui_objects:
            if obj.clickable and obj.x < m_x < obj.x + obj.width and m_y > obj.y and m_y < obj.y + obj.height:
                return obj
        return None