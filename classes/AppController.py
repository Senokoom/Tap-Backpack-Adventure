from DataManagment.SaveManager import SaveManager
from classes.Entities.Player import Player
from classes.GameState import GameState
from classes.Inventory.ActiveInventory import ActiveInventory
from classes.Inventory.BackpackInventory import BackpackInventory
from classes.System.settings import Config


class AppController:
    def __init__(self):
        self.state = GameState(self.create_player("Placeholder"))
        self.game_stated = False
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
            self.game_stated = True
            self.start_game_scene()
        except:
            self.FileError()
            return False

    def FileError(self):
        raise FileNotFoundError("Save file is Corrupted or Missing")


    def start_new_game(self, name):
        self.state = GameState(self.create_player(name))
        self.save_game()
        self.game_stated = True
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