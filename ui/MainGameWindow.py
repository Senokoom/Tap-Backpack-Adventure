import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QEvent, Qt
from PyQt6 import uic


class BattleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "main_battle.ui")
        uic.loadUi(ui_path, self)
