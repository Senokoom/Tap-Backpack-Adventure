import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class BattleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "main_battle.ui")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Tap Backpack Hero")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BattleWindow()
    window.show()
    sys.exit(app.exec())