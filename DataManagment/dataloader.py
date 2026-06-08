import yaml
from pathlib import Path

project_data_dir = Path(__file__).resolve().parent.parent / "data"


with open(project_data_dir / "weapons_en_ru.yaml", mode="r", encoding="utf-8") as weapons_data_file:
    weapon_data = yaml.safe_load(weapons_data_file)
with open(project_data_dir / "prefixes_en_ru.yaml", mode="r", encoding="utf-8") as prefixes_data_file:
    prefix_data = yaml.safe_load(prefixes_data_file)
with open(project_data_dir / "suffixes_en_ru.yaml", mode="r", encoding="utf-8") as suffix_data_file:
    suffix_data = yaml.safe_load(suffix_data_file)


with open(project_data_dir / "enemies.yaml", mode="r", encoding="utf-8") as enemy_data_file:
    enemy_data = yaml.safe_load(enemy_data_file)