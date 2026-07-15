import pygame
import gif_pygame

from ui.pyGame.Scenes.BattleScene import BattleScene
from ui.pyGame.Scenes.MainScene import MainScene
from ui.pyGame.UiElements.UiButton import UiButton
from ui.pyGame.UiElements.UiGifBackground import UiGifBackground
from ui.pyGame.UiElements.UiTextBox import UiTextBox
from ui.ui_config import UiConfig


class SceneManager:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.main_scene = ''
        self.scenes = {}
        self.current_scene = 0

        self.init_scenes()

    def init_scenes(self):
        self.main_scene = MainScene(
            "MainScene",
            self.app_controller,
            0
        )
        self.battle_scene = BattleScene(
            "BattleScene",
            self.app_controller,
            1
        )
        self.scenes['0'] = self.main_scene
        self.scenes['1'] = self.battle_scene

    def draw(self, surface):
        self.scenes[str(self.current_scene)].draw(surface)

    def update(self):
        self.scenes[str(self.current_scene)].update()

    def handle_event(self, event):
        self.scenes[str(self.current_scene)].handle_event(event)