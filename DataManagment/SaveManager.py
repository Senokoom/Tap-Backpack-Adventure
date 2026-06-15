import yaml
from classes.System.settings import Config
import os

class SaveManager:

    @staticmethod
    def save(game_state):
        if not os.path.exists(Config.save_dir):
            os.makedirs(Config.save_dir)
        save_path = os.path.join(Config.save_dir, Config.save_filename)
        with open(save_path, mode='w', encoding='utf-8') as save_file:
            yaml.dump(game_state.to_dict(), save_file, allow_unicode=True, default_flow_style=False, sort_keys=False)

    @staticmethod
    def load():
        save_path = os.path.join(Config.save_dir, Config.save_filename)
        if not os.path.exists(save_path):
            return None
        with open(save_path, 'r', encoding='utf-8') as load_file:
            data = yaml.safe_load(load_file)
        return data


