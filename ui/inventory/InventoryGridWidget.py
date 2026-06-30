from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel
from ui.inventory.SlotButton import SlotButton

class InventoryGridWidget(QWidget):
    grid_slot_clicked = pyqtSignal(str, int, int)
    def __init__(self, inv_name, width, height, controller, parent=None):
        super().__init__(parent)
        self.inv_name = inv_name
        self.width = width
        self.height = height

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)

        self.title_label = QLabel(inv_name)
        self.title_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #ddd;")
        self.layout.addWidget(self.title_label)

        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)

        self.selected_coords = None
        self.controller = controller

        self.cells = [[None for _ in range(width)] for _ in range(height)]

        for y in range(height):
            for x in range(width):
                slot = SlotButton(x, y)
                slot.slot_clicked.connect(lambda cx=x, cy=y: self._route_click(cx, cy))
                self.grid.addWidget(slot, y, x)
                self.cells[y][x] = slot

        self.layout.addLayout(self.grid)

    def refresh_from_controller(self):
        """Получает свежие данные у контроллера и обновляет все ячейки"""
        data_matrix = self.controller.get_inventory_ui_data(self.inv_name)

        # Определяем, какая ячейка сейчас должна быть подсвечена
        is_selected = lambda cx, cy: self.controller.selected_slot == (self.inv_name, cx, cy)

        for y in range(self.height):
            for x in range(self.width):
                item_data = data_matrix[y][x]
                slot = self.cells[y][x]

                if item_data:
                    slot.setText(item_data["name"][:10] + ".." if len(item_data["name"]) > 10 else item_data["name"])
                    self._apply_rarity_style(slot, item_data["rarity"])
                else:
                    slot.setText(f"{x},{y}")
                    self._apply_base_style(slot)

                # Подсветка выбирается динамически на основе состояния контроллера
                if is_selected(x, y):
                    self._apply_highlight_style(slot)

    def _apply_base_style(self, slot):
        slot.setStyleSheet("""
            QPushButton { background-color: #1e1e1e; border: 2px solid #444; 
                          border-radius: 6px; color: #888; font-size: 10px; }
        """)

    def _apply_rarity_style(self, slot, rarity):
        colors = {"common": "#888","uncommon": "#0bdb65", "rare": "#0070ff", "epic": "#a335ee", "legendary": "#ff8000"}
        color = colors.get(rarity, "#888")
        slot.setStyleSheet(f"""
            QPushButton {{ background-color: #1e1e1e; border: 2px solid {color}; 
                          border-radius: 6px; color: {color}; font-size: 10px; }}
        """)

    def _apply_highlight_style(self, slot):
        slot.setStyleSheet("""
            QPushButton { background-color: #2a3a2a; border: 2px solid #00ff88; 
                          border-radius: 6px; color: #00ff88; font-size: 10px; }
        """)


    def _route_click(self, x: int, y: int):
        print(f"✅ КЛИК ПОЙМАН: {self.inv_name} -> ({x}, {y})")

        # Снимаем выделение со старой
        if self.selected_coords:
            ox, oy = self.selected_coords
            self.cells[oy][ox].setStyleSheet(self._base_qss())

        # Ставим на новую
        self.selected_coords = (x, y)
        self.cells[y][x].setStyleSheet(self._highlight_qss())

        # Передаём в контроллер
        self.controller.on_inventory_slot_clicked(self.inv_name, x, y)
        self.grid_slot_clicked.emit(self.inv_name, x, y)

    def _base_qss(self):
        return """QPushButton { background-color: #1e1e1e; border: 2px solid #444; 
                    border-radius: 6px; color: #888; font-size: 10px; }"""

    def _highlight_qss(self):
        return """QPushButton { background-color: #2a3a2a; border: 2px solid #00ff88; 
                    border-radius: 6px; color: #00ff88; font-size: 10px; }"""

    def update_cell(self, x: int, y: int, item_name: str = None, rarity: str = "common"):
        colors = {"common": "#888","uncommon": "#0bdb65", "rare": "#0070ff", "epic": "#a335ee", "legendary": "#ff8000"}
        border = colors.get(rarity, "#888")
        text = item_name if item_name else f"{x},{y}"

        # Не перебиваем выделение, если ячейка сейчас активна
        if self.selected_coords == (x, y):
            return

        self.cells[y][x].setText(text)
        self.cells[y][x].setStyleSheet(f"""
            QLabel {{
                background-color: #1e1e1e;
                border: 2px solid {border};
                border-radius: 6px;
                color: {border};
                font-size: 10px;
            }}
        """)
