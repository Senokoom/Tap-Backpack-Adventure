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

        self.button_tap.clicked.connect(self.on_tap)
        self.frame_battle_area.installEventFilter(self)
        self.setWindowTitle("Tap Backpack Hero")

    def eventFilter(self, obj, event):
        # ПРАВИЛЬНОЕ сравнение через QEvent и Qt
        if obj is self.frame_battle_area and event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                print("Клик по фрейму!")
                return False  # Пропускаем событие дальше (если нужно)

        return super().eventFilter(obj, event)

    def on_tap(self):
        print("Тап по кнопке!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BattleWindow()
    window.show()
    sys.exit(app.exec())