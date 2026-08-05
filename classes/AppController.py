from DataManagment.SaveManager import SaveManager
from classes.Entities.Player import Player
from classes.GameState import GameState
from classes.Inventory.ActiveInventory import ActiveInventory
from classes.Inventory.BackpackInventory import BackpackInventory
from classes.System.settings import Config


class AppController:
    def __init__(self):
        self.state = GameState(self.create_player("Placeholder"))
        self.game_started = False
        self.scene_manager = None

    def set_scene_manager(self, scene_manager):
        self.scene_manager = scene_manager

    def switch_scene(self, scene):
        self.scene_manager.current_scene = scene


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
        try:
            self.state = GameState.from_dict(SaveManager.load())
            self.game_started = True
            self.start_game_scene()
        except:
            self.FileError()
            return False

    def FileError(self):
        raise FileNotFoundError("Save file is Corrupted or Missing")


    def start_new_game(self, name):
        self.state = GameState(self.create_player(name))
        self.save_game()
        self.game_started = True
        self.start_game_scene()

    def start_game_scene(self):
        self.switch_scene(1)

    def get_player_skill_points(self):
        return self.state.get_player_skill_points()

    def handle_tap(self):
        self.state.handle_tap()

    def get_last_damage(self):
        return self.state.get_player_last_damage()

    def get_enemy_hp_info(self):
        """
        Короче, возвращает кортеж из current_hp, max_hp(scaled) приведенные к int
        """
        max_hp = self.state.get_enemy_max_health()
        current_hp = self.state.get_enemy_current_hp()
        return int(current_hp), int(max_hp)

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

    def get_player_xp_to_next_level(self):
        return self.state.get_player_xp_to_next_level()

    def get_player_xp(self):
        return self.state.get_player_xp()

    def get_player_level(self):
        return self.state.get_player_level()

    def get_enemy_name(self):
        return self.state.get_enemy_name()

    def get_enemy_level(self):
        return self.state.get_enemy_level()

    def get_pending_item_list(self):
        return self.state.pending_loot

    def get_item_from_inventory_by_coordinates(self,x,y,inv_type):
        if inv_type == "active_inventory":
            return self.state.get_item_by_coordinates_from_active_inventory(x,y)
        elif inv_type == "backpack_inventory":
            return self.state.get_item_by_coordinates_from_backpack_inventory(x, y)
        return None

    def get_item_rotated(self, item, inv_type):
        if inv_type == "active_inventory":
            return self.state.rotate_item_active_inventory(item)
        elif inv_type == "backpack_inventory":
            return self.state.rotate_item_backpack_inventory(item)
        return None


    def get_item_move_by_player(self, x, y, item, inv_type):
        if inv_type == "active_inventory":
            return self.state.move_item_by_player_in_active_inventory(item, x, y)
        elif inv_type == "backpack_inventory":
            return self.state.move_item_by_player_in_backpack_inventory(item, x, y)
        return None


    def push_item_from_pending_into_active_inventory(self, item, x, y):
        return self.state.push_item_from_pending_in_inventory(x, y, item, "active_inventory")

    def get_inventory_ui_data(self, inv_type):
        if inv_type == "active_inventory":
            return self.state.get_active_inventory_ui_data()
        elif inv_type == "passive_inventory":
            return self.state.get_backpack_inventory_ui_data()
        return []