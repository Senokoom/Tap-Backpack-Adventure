from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal


class SlotButton(QPushButton):
    slot_clicked = pyqtSignal(int, int)  # Наш сигнал с координатами

    def __init__(self, x: int, y: int, parent=None):
        super().__init__(parent)
        self.x = x
        self.y = y

        # Убираем стандартный 3D-вид кнопки
        self.setFlat(True)
        self.setFixedSize(64, 64)

        # Базовый стиль (выглядит точно как твоя ячейка)
        self.setStyleSheet("""
            QPushButton {
                background-color: #1e1e1e;
                border: 2px solid #444;
                border-radius: 6px;
                color: #888;
                font-size: 10px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #2a2a2a;
                border: 2px solid #666;
            }
        """)
        self.setText(f"{x},{y}")

        # Нативный сигнал кнопки. Работает всегда, без mousePressEvent
        self.clicked.connect(self._emit_click)

    def _emit_click(self):
        self.slot_clicked.emit(self.x, self.y)