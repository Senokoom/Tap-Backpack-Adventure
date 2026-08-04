import pygame
import humanize

from classes.AppController import AppController
from ui.pyGame.Scenes.BaseScene import BaseScene
from ui.pyGame.Scenes.MainScene import MainScene
from ui.pyGame.UiElements.UiButton import UiButton
from ui.pyGame.UiElements.UiImage import UiImage
from ui.pyGame.UiElements.UiBattleBackground import UiBattleBackground
from ui.pyGame.UiElements.UiEnemy import UiEnemy
from ui.pyGame.UiElements.UiLabel import UiLabel
from ui.pyGame.UiElements.UiLevelUp import UiLevelUp
from ui.pyGame.UiElements.UiRectangle import UiRectangle
from ui.ui_config import UiConfig


class BattleScene(BaseScene):
    def __init__(self, name, controller: AppController, number):
        self.name = name
        self.controller = controller
        self.number = number

        self.ui_objects = []

        self.dps = 0

        self.show_level_up_value = True

        self.enemy = None

        self.ui_objects.append(battle_background:=UiBattleBackground(160, 20, pygame.image.load(UiConfig.battle_background_path),
                                                                     (500, 230), list(map(pygame.image.load, UiConfig.clouds_path)), 1, self.controller.handle_tap))
        self.battle_background = battle_background

        self.ui_objects.append(enemy := UiEnemy(410, 210, 130, UiConfig.slime_idle, UiConfig.slime_hit, UiConfig.slime_die, controller))

        self.ui_objects.append(coin_label := UiLabel(50, 32, 100, 100, pygame.font.Font(UiConfig.game_font, 30), controller.get_player_gold(), (255,255,0)))
        self.ui_objects.append(UiImage(12, 30, pygame.image.load(UiConfig.coin_path), (35, 35), 1))

        self.ui_objects.append(dps_label := UiLabel(20, 90, 100, 100, pygame.font.Font(UiConfig.game_font, 20), "DPS: 0.00", (255, 100, 100)))

        self.ui_objects.append(lvl_label := UiLabel(680, 30, 100, 100, pygame.font.Font(UiConfig.game_font, 25), "Lvl:", (100, 255, 100)))

        self.ui_objects.append(lvlup_label := UiLevelUp(700, 90, 70, 55, pygame.font.Font(UiConfig.game_font, 50), (100,255,100), self.controller.get_player_skill_points(), self.label_func_level_up_show))


        self.ui_objects.append(levelup_rect := UiRectangle(100, 260, 600, 300, (100, 25, 25)))
        self.ui_objects.append(physical_label := UiLabel(110, 270, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Physical Damage: ", (255, 255, 255)))
        self.ui_objects.append(fire_label := UiLabel(110, 295, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Fire Damage: ", (255, 255, 255)))
        self.ui_objects.append(ice_label := UiLabel(110, 320, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Ice Damage: ", (255, 255, 255)))
        self.ui_objects.append(lightning_label := UiLabel(110, 345, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Lightning Damage: ", (255, 255, 255)))
        self.ui_objects.append(emotional_label := UiLabel(110, 370, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Emotional Damage: ", (255, 255, 255)))
        self.ui_objects.append(critical_label := UiLabel(110, 395, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Critical Damage: ", (255, 255, 255)))
        self.ui_objects.append(critical_chance_label := UiLabel(110, 420, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Critical Damage Chance: ", (255, 255, 255)))
        self.ui_objects.append(item_drop_label := UiLabel(110, 445, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Item Drop Chance: ", (255, 255, 255)))
        self.ui_objects.append(rare_item_chance_label := UiLabel(110, 470, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                          "Rare Item Chance: ", (255, 255, 255)))
        self.ui_objects.append(gold_drop_label := UiLabel(110, 495, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "Gold Drop: ", (255, 255, 255)))
        self.ui_objects.append(xp_drop_label := UiLabel(110, 520, 100, 100, pygame.font.Font(UiConfig.game_font, 20),

                                                          "Xp Drop: ", (255, 255, 255)))

        self.ui_objects.append(physical_lvl_label := UiLabel(410, 270, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "", (255, 255, 255)))
        self.ui_objects.append(fire_lvl_label := UiLabel(410, 295, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                     "", (255, 255, 255)))
        self.ui_objects.append(ice_lvl_label := UiLabel(410, 320, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                    "", (255, 255, 255)))
        self.ui_objects.append(lightning_lvl_label := UiLabel(410, 345, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                          "", (255, 255, 255)))
        self.ui_objects.append(emotional_lvl_label := UiLabel(410, 370, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                          "", (255, 255, 255)))
        self.ui_objects.append(critical_lvl_label := UiLabel(410, 395, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                         "", (255, 255, 255)))
        self.ui_objects.append(
            critical_chance_lvl_label := UiLabel(410, 420, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                             "", (255, 255, 255)))
        self.ui_objects.append(item_drop_lvl_label := UiLabel(410, 445, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                          "", (255, 255, 255)))
        self.ui_objects.append(
            rare_item_chance_lvl_label := UiLabel(410, 470, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                              "", (255, 255, 255)))
        self.ui_objects.append(gold_drop_lvl_label := UiLabel(410, 495, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                          "", (255, 255, 255)))
        self.ui_objects.append(xp_drop_lvl_label := UiLabel(410, 520, 100, 100, pygame.font.Font(UiConfig.game_font, 20),
                                                        "", (255, 255, 255)))

        self.ui_objects.append(physical_button := UiButton("", 640, 270, 40, 20,(25, 100, 25), pygame.font.Font(UiConfig.game_font, 30),
                                                         "+", 0, self.level_up_physical, border_radius=2))
        self.ui_objects.append(fire_button := UiButton("", 640, 295, 40, 20, (25, 100, 25),
                                                           pygame.font.Font(UiConfig.game_font, 30),
                                                           "+", 0, self.level_up_fire, border_radius=2))
        self.ui_objects.append(ice_button := UiButton("", 640, 320, 40, 20, (25, 100, 25),
                                                           pygame.font.Font(UiConfig.game_font, 30),
                                                           "+", 0, self.level_up_ice, border_radius=2))
        self.ui_objects.append(lightning_button := UiButton("", 640, 345, 40, 20, (25, 100, 25),
                                                       pygame.font.Font(UiConfig.game_font, 30),
                                                       "+", 0, self.level_up_lightning, border_radius=2))
        self.ui_objects.append(emotional_button := UiButton("", 640, 370, 40, 20, (25, 100, 25),
                                                           pygame.font.Font(UiConfig.game_font, 30),
                                                           "+", 0, self.level_up_emotional, border_radius=2))
        self.ui_objects.append(critical_button := UiButton("", 640, 395, 40, 20, (25, 100, 25),
                                                       pygame.font.Font(UiConfig.game_font, 30),
                                                       "+", 0, self.level_up_critical, border_radius=2))
        self.ui_objects.append(critical_chance_button := UiButton("", 640, 420, 40, 20, (25, 100, 25),
                                                           pygame.font.Font(UiConfig.game_font, 30),
                                                           "+", 0, self.level_up_critical_chance, border_radius=2))
        self.ui_objects.append(gold_drop_button := UiButton("", 640, 445, 40, 20, (25, 100, 25),
                                                       pygame.font.Font(UiConfig.game_font, 30),
                                                       "+", 0, self.level_up_gold_drop, border_radius=2))
        self.ui_objects.append(xp_drop_button := UiButton("", 640, 470, 40, 20, (25, 100, 25),
                                                           pygame.font.Font(UiConfig.game_font, 30),
                                                           "+", 0, self.level_up_xp_drop, border_radius=2))
        self.ui_objects.append(item_drop_button := UiButton("", 640, 495, 40, 20, (25, 100, 25),
                                                       pygame.font.Font(UiConfig.game_font, 30),
                                                       "+", 0, self.level_up_item_drop, border_radius=2))
        self.ui_objects.append(rare_item_drop_button := UiButton("", 640, 520, 40, 20, (25, 100, 25),
                                                            pygame.font.Font(UiConfig.game_font, 30),
                                                            "+", 0, self.level_up_rare_item_drop, border_radius=2))


        # {'physical_damage': 1,
        # 'fire_damage': 1,
        # 'ice_damage': 1,
        # 'lightning_damage': 1,
        # 'emotional_damage': 1,
        # 'critical_damage': 0.5,
        # 'critical_damage_chance': 0.05,
        # 'gold_drop': 1.0,
        # 'xp_drop': 1.0,
        # 'item_drop': 0.1,
        # 'rare_item_chance': 0.05}


        self.level_labels = [
            physical_lvl_label,
            fire_lvl_label,
            ice_lvl_label,
            lightning_lvl_label,
            emotional_lvl_label,
            critical_lvl_label,
            critical_chance_lvl_label,
            gold_drop_lvl_label,
            xp_drop_lvl_label,
            item_drop_lvl_label,
            rare_item_chance_lvl_label
        ]


        for level in self.level_labels:
            level.x += 40

        self.level_upgrade_list = [
            levelup_rect,
            physical_label,
            fire_label,
            ice_label,
            lightning_label,
            emotional_label,
            critical_label,
            item_drop_label,
            gold_drop_label,
            critical_chance_label,
            rare_item_chance_label,
            xp_drop_label,
            physical_lvl_label,
            fire_lvl_label,
            ice_lvl_label,
            lightning_lvl_label,
            emotional_lvl_label,
            critical_lvl_label,
            item_drop_lvl_label,
            gold_drop_lvl_label,
            critical_chance_lvl_label,
            rare_item_chance_lvl_label,
            xp_drop_lvl_label,
            physical_button,
            fire_button,
            ice_button,
            lightning_button,
            emotional_button,
            critical_button,
            critical_chance_button,
            gold_drop_button,
            item_drop_button,
            rare_item_drop_button,
            xp_drop_button
        ]

        self.show_inventory()

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
        if self.level_labels:
            level_values_list = list(self.controller.get_player_base_stats().values())
            for i in range(len(self.level_labels)):
                self.level_labels[i].text = f"{level_values_list[i]:.2f}"
        if self.controller.get_player_skill_points() > 0:
            self.lvlup_label.show = True
        else:
            self.show_inventory()
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
            if self.clicked_obj and self.clicked_obj.show:
                if isinstance(self.clicked_obj, UiBattleBackground):
                    self.dps += self.controller.get_last_damage()
                    self.clicked_obj.execute(pygame.mouse.get_pos())
                else:
                    self.clicked_obj.execute()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked_obj = MainScene.checkIntersection(self.ui_objects, pygame.mouse.get_pos())
            if self.clicked_obj:
                self.clicked_obj.clicked = True

    def level_up_physical(self):
        self.controller.get_player_level_up("physical_damage")

    def level_up_fire(self):
        self.controller.get_player_level_up("fire_damage")

    def level_up_ice(self):
        self.controller.get_player_level_up("ice_damage")

    def level_up_lightning(self):
        self.controller.get_player_level_up("lightning_damage")

    def level_up_emotional(self):
        self.controller.get_player_level_up("emotional_damage")

    def level_up_critical(self):
        self.controller.get_player_level_up("critical_damage")

    def level_up_gold_drop(self):
        self.controller.get_player_level_up("gold_drop")

    def level_up_critical_chance(self):
        self.controller.get_player_level_up("critical_damage_chance")

    def level_up_xp_drop(self):
        self.controller.get_player_level_up("xp_drop")

    def level_up_item_drop(self):
        self.controller.get_player_level_up("item_drop")

    def level_up_rare_item_drop(self):
        self.controller.get_player_level_up("rare_item_chance")


    def label_func_level_up_show(self):
        if self.show_level_up_value:
            self.show_level_up()
            self.show_level_up_value = False
        else:
            self.show_level_up_value = True
            self.show_inventory()

    def show_inventory(self):
        for obj in self.level_upgrade_list:
            obj.show = False

    def show_level_up(self):
        for obj in self.level_upgrade_list:
            obj.show = True
