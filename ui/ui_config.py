
import yaml
from pathlib import Path

from DataManagment.dataloader import project_data_dir


class ImagePaths:
    project_data_dir = Path(__file__).resolve().parent
    with open(project_data_dir / 'ui_config.yaml', mode="r", encoding="utf-8") as settings:
        image_paths = yaml.safe_load(settings)

    logo_path = project_data_dir / image_paths["ui"]["logo_path"]
    main_menu_gif_path = project_data_dir / image_paths["ui"]["main_menu_gif_path"]

    game_font = project_data_dir / image_paths["ui"]["font"]