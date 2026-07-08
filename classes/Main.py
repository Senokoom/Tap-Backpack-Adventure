import sys
from PyQt6.QtWidgets import QApplication

from ui.pyGame.game import PyGameWindow
from ui.pyQt.main_window import MainWindow
from classes.AppController import AppController

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = MainWindow(AppController())
    # window.show()
    # sys.exit(app.exec())
    game = PyGameWindow(AppController)