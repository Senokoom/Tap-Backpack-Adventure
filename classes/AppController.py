from DataManagment.SaveManager import SaveManager
from classes.Entities.Player import Player
from classes.GameState import GameState
from classes.Inventory.ActiveInventory import ActiveInventory
from classes.Inventory.BackpackInventory import BackpackInventory
from classes.System.settings import Config


class AppController:
    def __init__(self):
        self.state = GameState(self.create_player("Placeholder"))
        # self.selected_slot = None

    # def get_inventory_ui_data(self, inv_type: str) -> list[list[dict | None]]:
    #     """Возвращает 2D-матрицу только для отрисовки. UI не лезет в GameState."""
    #     inv = self._get_inventory(inv_type)
    #     matrix = []
    #     for row in inv.inventory_matrix:
    #         ui_row = []
    #         for cell in row:
    #             if cell and cell.item:
    #                 ui_row.append({
    #                     "name": cell.item.name,
    #                     "rarity": getattr(cell.item, "rarity", "common")
    #                 })
    #             else:
    #                 ui_row.append(None)
    #         matrix.append(ui_row)
    #     return matrix
    #
    # def _get_inventory(self, inv_type: str):
    #     """Вспомогательный метод: возвращает нужный инвентарь"""
    #     return self.state.player.ActiveInventory if inv_type == "Active Inventory" else self.state.player.BackpackInventory
    #
    # def handle_inventory_click(self, inv_type: str, x: int, y: int):
    #     """Логика клика: выбор -> перемещение -> сброс"""
    #     inv = self._get_inventory(inv_type)
    #     target_cell = inv.inventory_matrix[y][x]
    #
    #     # 1. Если ничего не выбрано
    #     if self.selected_slot is None:
    #         if target_cell and target_cell.item:
    #             self.selected_slot = (inv_type, x, y)  # Запоминаем координаты
    #             return "selected"
    #         return "empty"
    #
    #     # 2. Если что-то уже выбрано
    #     sel_inv_type, sel_x, sel_y = self.selected_slot
    #     sel_inv = self._get_inventory(sel_inv_type)
    #     source_cell = sel_inv.inventory_matrix[sel_y][sel_x]
    #
    #     # Кликнули на ту же ячейку → снять выделение
    #     if sel_inv_type == inv_type and sel_x == x and sel_y == y:
    #         self.selected_slot = None
    #         return "deselected"
    #
    #     # Перемещаем предмет
    #     if target_cell is None or not target_cell.item:
    #         # Пустая ячейка → переносим
    #         target_cell.item = source_cell.item
    #         source_cell.item = None
    #         self.selected_slot = None
    #         return "moved"
    #     else:
    #         # Занятая ячейка → меняем местами
    #         target_cell.item, source_cell.item = source_cell.item, target_cell.item
    #         self.selected_slot = None
    #         return "swapped"
    #

    def get_player_level_up(self, skill):
        self.state.get_player_level_up(skill)
    def create_player(self, name):
        return Player(
            1,
            name,
            Config.new_game_player_stats["xppoints"],
            Config.new_game_player_stats["gold"],
            Config.new_game_player_stats["level"],
            Config.new_game_player_stats["skill_point"],
            ActiveInventory(Config.new_game_active_inventory["width"], Config.new_game_active_inventory["height"]),
            BackpackInventory(Config.new_game_backpack_inventory["width"],
                              Config.new_game_backpack_inventory["height"]),
            Config.new_game_player_stats["last_time_online"],
            None,
            Config.new_game_player_stats["stats"]
        )

    def get_active_inventory_width_height(self):
        return self.state.get_active_inventory_width_height()

    def save_game(self):
        SaveManager.save(self.state)

    def load_game(self):
        self.state = GameState.from_dict(SaveManager.load())

    def start_new_game(self, name):
        self.state = GameState(self.create_player(name))
        self.save_game()

    def get_player_skill_points(self):
        return self.state.get_player_skill_points()

    def handle_tap(self):
        self.state.handle_tap()

    def get_last_damage(self):
        return self.state.get_player_last_damage()

    def get_enemy_hp_info(self):
        """
        Короче, возвращает кортеж из current_hp, max_hp(scaled), percentage(осталось)
        """
        max_hp = self.state.get_enemy_max_health()
        current_hp = self.state.get_enemy_current_hp()
        return current_hp, max_hp, int((current_hp/max_hp)*100)

    def get_player_current_stats(self):
        """
        После бонусов от оружия. Возвращает Dict
        """
        return self.state.get_player_current_stats()

    def get_player_base_stats(self):
        """
        До бонусов от оружия, возможно потом буду скейлить их с помощью xp_points
        :return: возвращает dict
        """
        return self.state.get_player_base_stats()

    def get_player_name(self):
        return self.state.get_player_name()

    def get_player_gold(self):
        return self.state.get_player_gold()

    def get_player_xp(self):
        return self.state.get_player_xp()

    def get_player_level(self):
        return self.state.get_player_level()

    def get_enemy_name(self):
        return self.state.get_enemy_name()

    def get_enemy_level(self):
        return self.state.get_enemy_level()

    def get_inventory_ui_data(self, inv_type):
        if inv_type == "Active Inventory":
            return self.state.get_active_inventory_ui_data()
        elif inv_type == "Backpack":
            return self.state.get_backpack_inventory_ui_data()
        return []