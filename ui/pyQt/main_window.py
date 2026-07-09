from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from PyQt6 import uic

import os

from classes.AppController import AppController
from classes.System.settings import Config


class MainWindow(QMainWindow):
    def __init__(self, controller: AppController):
        super().__init__()
        self.controller = controller
        self.load_ui()
        self.setup_initial_state()

    def load_ui(self):
        ui_path = os.path.join(os.path.dirname(__file__), "TapBackpackQT.ui")
        uic.loadUi(ui_path, self)
        self.setup_connections()

    def setup_connections(self):
        self.new_game_button.clicked.connect(self.new_game_clicked)
        self.load_game_button.clicked.connect(self.load_game_clicked)
        self.tap_button.clicked.connect(self.tap_button_clicked)
        self.save_button.clicked.connect(self.tap_save_button)

        self.physical_up_button.clicked.connect(self.level_button_click)
        self.fire_up_button.clicked.connect(self.level_button_click)
        self.critical_chance_up_button.clicked.connect(self.level_button_click)
        self.critical_up_button.clicked.connect(self.level_button_click)
        self.emotional_up_button.clicked.connect(self.level_button_click)
        self.gold_up_button.clicked.connect(self.level_button_click)
        self.ice_up_button.clicked.connect(self.level_button_click)
        self.item_drop_up_button.clicked.connect(self.level_button_click)
        self.lightning_up_button.clicked.connect(self.level_button_click)
        self.rare_item_up_button.clicked.connect(self.level_button_click)
        self.xp_drop_up_button.clicked.connect(self.level_button_click)

        self.get_back_levelup_button.clicked.connect(self.get_back_to_fight)
        self.level_button.clicked.connect(self.level_page_button_click)
        # self.inventory_button.clicked.connect(self.tap_inventory_button)
        # self.active_grid.grid_slot_clicked.connect(self.on_inventory_click)
        # self.backpack_grid.grid_slot_clicked.connect(self.on_inventory_click)

    # def on_inventory_click(self, inv_type: str, x: int, y: int):
    #     status = self.controller.handle_inventory_click(inv_type, x, y)
    #
    #     # После любой логики обновляем ОБЕ сетки
    #     self.active_grid.refresh_from_controller()
    #     self.backpack_grid.refresh_from_controller()

    def get_back_to_fight(self):
        self.stackedWidget.setCurrentIndex(1)
        self.update_ui_after_tap()

    def tap_save_button(self):
        self.controller.save_game()

    def setup_initial_state(self):
        self.stackedWidget.setCurrentIndex(0)
        if not os.path.exists(os.path.join(Config.save_dir, Config.save_filename)):
            self.load_game_button.setEnabled(False)
            self.load_game_button.setText("Нет сохранения")
        else:
            self.load_game_button.setEnabled(True)

    def load_game_clicked(self):
        try:
            self.controller.load_game()
            self.stackedWidget.setCurrentIndex(1)
            self.update_ui_after_tap()
        except:
            self.load_game_button.setEnabled(False)
            self.load_game_button.setText("Сохранение повреждено")

    def new_game_clicked(self):
        if not self.input_hero_name.default_text():
            return
        else:
            self.controller.start_new_game(self.input_hero_name.default_text())
            self.stackedWidget.setCurrentIndex(1)
            self.update_ui_after_tap()


    def update_ui_after_tap(self):
        self.player_name_label.setText(f"Player: {self.controller.get_player_name()}")
        self.damage_dealt_label.setText(f"Damage: {self.controller.get_last_damage():.0f}")
        current_hp, max_hp, percentage = self.controller.get_enemy_hp_info()
        self.enemy_health_progress_bar.setValue(percentage)
        self.enemy_health_label.setText(f"{current_hp:.0f}/{max_hp:.0f}")
        self.gold_label.setText(f"Gold: {self.controller.get_player_gold():.0f}")
        self.xp_label.setText(f"Total xp: {self.controller.get_player_xp():.0f}")
        self.player_level_label.setText(f"Player level: {self.controller.get_player_level():.0f}")
        self.enemy_name_label.setText(f"Enemy name: {self.controller.get_enemy_name()}  Level: {self.controller.get_enemy_level()}")
        current_stats = ""
        for key, value in self.controller.get_player_current_stats().items():
            current_stats += f"{key}: {value}\n"
        self.current_player_stats.setText(f"Current Stats: \n{current_stats}")



    def level_up_ui_update(self):
        current_stats = ""
        for key, value in self.controller.get_player_current_stats().items():
            current_stats += f"{key}: {value}\n"
        self.stats_level_up_label.setText(f"Current Stats: \n{current_stats}")
        self.skill_points_label.setText(f"Skill Points: {self.controller.get_player_skill_points()}")

    def level_page_button_click(self):
        self.stackedWidget.setCurrentIndex(2)
        self.level_up_ui_update()


    def level_button_click(self):
        self.controller.get_player_level_up(self.sender().property("stat"))
        self.level_up_ui_update()

    def tap_button_clicked(self):
        self.controller.handle_tap()
        self.update_ui_after_tap()

