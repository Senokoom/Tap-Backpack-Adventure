from PyQt6.QtWidgets import QMainWindow, QGridLayout
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
            self.player_name_label.setText(f"Player: {self.controller.get_player_name()}")
        except:
            self.load_game_button.setEnabled(False)
            self.load_game_button.setText("Сохранение повреждено")

    def new_game_clicked(self):
        if not self.input_hero_name.text():
            return
        else:
            self.controller.start_new_game(self.input_hero_name.text())
            self.stackedWidget.setCurrentIndex(1)


    def update_ui_after_tap(self):
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



    def tap_button_clicked(self):
        self.controller.handle_tap()
        self.update_ui_after_tap()

