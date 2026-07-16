import pygame

from classes.AppController import AppController
from ui.pyGame.Scenes.BaseScene import BaseScene
from ui.pyGame.Scenes.MainScene import MainScene
from ui.pyGame.UiElements.UiBattleBackground import UiBattleBackground
from ui.pyGame.UiElements.UiButton import UiButton
from ui.pyGame.UiElements.UiProgressBar import UiProgressBar
from ui.ui_config import UiConfig


class BattleScene(BaseScene):
    def __init__(self, name, controller: AppController, number):
        self.name = name
        self.controller = controller
        self.number = number

        self.ui_objects = []



        self.ui_objects.append(UiBattleBackground(160, 20, pygame.image.load(UiConfig.battle_background_path), (500, 230), list(map(pygame.image.load, UiConfig.clouds_path)), 1, self.controller.handle_tap))
        self.ui_objects.append(hp_bar := UiProgressBar(210, 30, 400, 30, (255, 0,0),
                                             (0,0,0), 500, 400, pygame.font.Font(UiConfig.game_font, 20)))
        self.hp_bar = hp_bar

        self.clicked_obj = None

    #debug func
    def take_damage(self):
        self.hp_bar.progress_bar_value -= 10

    def draw(self, surface):
        for obj in self.ui_objects:
            if obj.show:
                obj.draw(surface)

    def update(self):
        for obj in self.ui_objects:
            obj.update()
        self.hp_bar.progress_bar_value, self.hp_bar.progress_bar_max = self.controller.get_enemy_hp_info()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.clicked_obj = MainScene.checkIntersection(self.ui_objects, pygame.mouse.get_pos())
            for obj in self.ui_objects:
                obj.clicked = False
            if self.clicked_obj:
                self.clicked_obj.execute()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked_obj = MainScene.checkIntersection(self.ui_objects, pygame.mouse.get_pos())
            if self.clicked_obj:
                self.clicked_obj.clicked = True