import pygame
import humanize

from classes.AppController import AppController
from ui.pyGame.Scenes.BaseScene import BaseScene
from ui.pyGame.Scenes.MainScene import MainScene
from ui.pyGame.UiElements.UiImage import UiImage
from ui.pyGame.UiElements.UiBattleBackground import UiBattleBackground
from ui.pyGame.UiElements.UiEnemy import UiEnemy
from ui.pyGame.UiElements.UiLabel import UiLabel
from ui.pyGame.UiElements.UiLevelUp import UiLevelUp
from ui.ui_config import UiConfig


class BattleScene(BaseScene):
    def __init__(self, name, controller: AppController, number):
        self.name = name
        self.controller = controller
        self.number = number

        self.ui_objects = []

        self.dps = 0

        self.enemy = None

        self.ui_objects.append(battle_background:=UiBattleBackground(160, 20, pygame.image.load(UiConfig.battle_background_path),
                                                                     (500, 230), list(map(pygame.image.load, UiConfig.clouds_path)), 1, self.controller.handle_tap))
        self.battle_background = battle_background

        self.ui_objects.append(enemy := UiEnemy(410, 210, 130, UiConfig.slime_idle, UiConfig.slime_hit, UiConfig.slime_die, controller))

        self.ui_objects.append(coin_label := UiLabel(50, 32, 100, 100, pygame.font.Font(UiConfig.game_font, 30), controller.get_player_gold(), (255,255,0)))
        self.ui_objects.append(UiImage(12, 30, pygame.image.load(UiConfig.coin_path), (35, 35), 1))

        self.ui_objects.append(dps_label := UiLabel(20, 90, 100, 100, pygame.font.Font(UiConfig.game_font, 20), "DPS: 0.00", (255, 100, 100)))

        self.ui_objects.append(lvl_label := UiLabel(680, 30, 100, 100, pygame.font.Font(UiConfig.game_font, 25), "Lvl:", (100, 255, 100)))

        self.ui_objects.append(lvlup_label := UiLevelUp(700, 90, 70, 55, pygame.font.Font(UiConfig.game_font, 50), (100,255,100), self.controller.get_player_skill_points()))

        if self.controller.get_player_skill_points() <= 0:
            lvlup_label.show = False
        self.lvlup_label = lvlup_label
        self.lvl_label = lvl_label
        self.dps_label = dps_label
        self.coin_label = coin_label
        self.enemy = enemy

        self.clicked_obj = None

        self.timer_start = pygame.time.get_ticks()



    def draw(self, surface):
        for obj in self.ui_objects:
            if obj.show:
                obj.draw(surface)


    def update(self):
        if self.controller.get_player_skill_points() > 0:
            self.lvlup_label.show = True
        else:
            self.lvlup_label.show = False
        self.lvlup_label.points_amount = self.controller.get_player_skill_points()
        if pygame.time.get_ticks() - self.timer_start >= 1000:
            self.dps_label.text = f"DPS: {humanize.metric(self.dps)}"
            self.dps = 0
            self.timer_start = pygame.time.get_ticks()
        self.lvl_label.text = f"Lvl: {self.controller.get_player_level() if not self.controller.get_player_level()//1000 else "\n" + str(self.controller.get_player_level())}"
        for obj in self.ui_objects:
            obj.update()
        self.coin_label.text = humanize.metric(self.controller.get_player_gold())
        self.battle_background.enemy = self.enemy


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.clicked_obj = MainScene.checkIntersection(self.ui_objects, pygame.mouse.get_pos())
            for obj in self.ui_objects:
                obj.clicked = False
            if self.clicked_obj:
                if isinstance(self.clicked_obj, UiBattleBackground):
                    self.dps += self.controller.get_last_damage()
                    self.clicked_obj.execute(pygame.mouse.get_pos())
                else:
                    self.clicked_obj.execute()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked_obj = MainScene.checkIntersection(self.ui_objects, pygame.mouse.get_pos())
            if self.clicked_obj:
                self.clicked_obj.clicked = True