import pygame

from ui.pyGame.Scenes.BaseScene import BaseScene
from ui.pyGame.UiElements.UiBattleBackground import UiBattleBackground
from ui.ui_config import UiConfig


class BattleScene(BaseScene):
    def __init__(self, name, controller, number):
        self.name = name
        self.controller = controller
        self.number = number

        self.ui_objects = []

        self.ui_objects.append(UiBattleBackground(160, 20, pygame.image.load(UiConfig.battle_background_path), (500, 230), list(map(pygame.image.load, UiConfig.clouds_path)), 1))


    def draw(self, surface):
        for obj in self.ui_objects:
            if obj.show:
                obj.draw(surface)

    def update(self):
        for obj in self.ui_objects:
            obj.update()