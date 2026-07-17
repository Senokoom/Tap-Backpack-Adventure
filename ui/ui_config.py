
import yaml
from pathlib import Path

from DataManagment.dataloader import project_data_dir


class UiConfig:
    project_data_dir = Path(__file__).resolve().parent
    with open(project_data_dir / 'ui_config.yaml', mode="r", encoding="utf-8") as settings:
        image_paths = yaml.safe_load(settings)

    logo_path = project_data_dir / image_paths["ui"]["logo_path"]
    main_menu_gif_path = project_data_dir / image_paths["ui"]["main_menu_gif_path"]

    battle_background_path = project_data_dir / image_paths["ui"]["battle_background_path"]
    clouds_path = [project_data_dir / image_paths["ui"]["cloud_1_path"], project_data_dir / image_paths["ui"]["cloud_2_path"], project_data_dir / image_paths["ui"]["cloud_3_path"]]

    game_font = project_data_dir / image_paths["ui"]["font"]

    slime_hit = project_data_dir / image_paths["ui"]["entities"]["slime"]["hit"]
    slime_idle = project_data_dir / image_paths["ui"]["entities"]["slime"]["idle"]
    slime_die = project_data_dir / image_paths["ui"]["entities"]["slime"]["die"]
