import pygame
import sys

from gif_pygame import gif_pygame

from classes.AppController import AppController
from ui.pyGame.UiElements.UiBattleBackground import UiBattleBackground
from ui.pyGame.UiElements.UiGifBackground import UiGifBackground
from ui.pyGame.UiElements.UiTextBox import UiTextBox
from ui.ui_config import UiConfig
from ui.pyGame.UiElements.UiAnimatedLogo import UiAnimatedLogo
from ui.pyGame.UiElements.UiButton import UiButton


class PyGameWindow:
    def __init__(self, app_controller: AppController, window=1):
        """
        :param window: текущее окно.
        0 - Главное меню
        1 - Окно игры
        """
        pygame.init()
        self.controller = app_controller
        self.screen = pygame.display.set_mode((800, 600))

        self.main_menu_color = (16, 11, 11)

        self.objects = []
        self.objects_on_screen = []
        self.window = window

        self.init_objects()
        self.init_objects_on_screen()

        self.clock = pygame.time.Clock()
        self.main_loop()


    def init_objects(self):
        self.objects.append(UiGifBackground(100, 0, gif_pygame.load(UiConfig.main_menu_gif_path), (800, 600), 0))
        self.objects.append(UiAnimatedLogo(15, 20, pygame.image.load(UiConfig.logo_path), 0))
        self.objects.append(UiButton("LoadGame", 90, 480, 180, 70, (63, 110, 30),
                                     pygame.font.Font(UiConfig.game_font, 20), "Load Game", 0,
                                     lambda: self.controller.load_game(), 0, (16, 6, 6)))
        text_box = UiTextBox(60, 300, 250, 50, (205,205,205), pygame.font.Font(UiConfig.game_font, 25), 0, (16, 6, 6))
        self.objects.append(text_box)
        self.objects.append(UiButton("NewGame", 90, 380, 180, 70, (153, 90, 8),
                                     pygame.font.Font(UiConfig.game_font, 20), "New Game", 0,
                                     lambda: self.controller.start_new_game(text_box.text) if text_box.text != "" else "Can't Create Hero Without A Name",
                                     0, (16, 6, 6)))

        self.objects.append(UiBattleBackground(160, 20, pygame.image.load(UiConfig.battle_background_path), (500, 230), list(map(pygame.image.load, UiConfig.clouds_path)), 1))



    def init_objects_on_screen(self):
        self.objects_on_screen = []
        for obj in self.objects:
            if obj.screen == self.window:
                self.objects_on_screen.append(obj)
        return self.objects_on_screen


    def main_loop(self):
        clicked_obj = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if clicked_obj and isinstance(clicked_obj, UiTextBox):
                        clicked_obj.update(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    clicked_obj = self.checkIntersection(pygame.mouse.get_pos())
                    for obj in self.objects_on_screen:
                        obj.clicked = False
                    if clicked_obj and isinstance(clicked_obj, UiTextBox):
                        clicked_obj.clicked = True
                    elif clicked_obj and isinstance(clicked_obj, UiButton):
                        clicked_obj.action()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_obj = self.checkIntersection(pygame.mouse.get_pos())
                    if clicked_obj:
                        clicked_obj.clicked = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw()
            dt = self.clock.tick(160)
            pygame.display.flip()

    def draw(self):
        self.screen.fill(self.main_menu_color)
        for obj in self.objects_on_screen:
            obj.draw(self.screen)


    def checkIntersection(self, mxy: tuple) -> UiButton | None:
        m_x, m_y = mxy
        for obj in self.objects_on_screen:
            if obj.clickable and obj.x < m_x < obj.x + obj.width and m_y > obj.y and m_y < obj.y + obj.height:
                return obj
        return None