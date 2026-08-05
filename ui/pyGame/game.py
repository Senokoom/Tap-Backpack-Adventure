import pygame
import sys

from gif_pygame import gif_pygame

from classes.AppController import AppController
from ui.pyGame.Scenes.SceneManager import SceneManager
from ui.pyGame.UiElements.UiBattleBackground import UiBattleBackground
from ui.pyGame.UiElements.UiGifBackground import UiGifBackground
from ui.pyGame.UiElements.UiTextBox import UiTextBox
from ui.ui_config import UiConfig
from ui.pyGame.UiElements.UiAnimatedLogo import UiAnimatedLogo
from ui.pyGame.UiElements.UiButton import UiButton


class PyGameWindow:
    def __init__(self, app_controller: AppController, window=0):
        """
        :param window: текущее окно.
        0 - Главное меню
        1 - Окно игры
        """
        pygame.init()
        self.controller = app_controller
        self.screen = pygame.display.set_mode((800, 600))

        self.main_menu_color = (16, 11, 11)
        self.window = window
        self.clock = pygame.time.Clock()

        self.scene_manager = SceneManager(self.controller)
        self.controller.set_scene_manager(self.scene_manager)

        self.animation_speed = 1
        self.counter = 1

        self.main_loop()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                self.scene_manager.handle_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw()
            dt = self.clock.tick(165)
            pygame.display.flip()


    def draw(self):
        self.screen.fill(self.main_menu_color)
        if self.counter % self.animation_speed == 0:
            self.update()
            counter = 0
        self.scene_manager.draw(self.screen)

    def update(self):
        self.scene_manager.update()
