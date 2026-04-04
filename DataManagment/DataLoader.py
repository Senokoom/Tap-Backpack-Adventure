import yaml
from pathlib import Path

project_data_dir = Path(__file__).resolve().parent.parent / "data"
print(project_data_dir)


with open(project_data_dir / "weapons_en_ru.yaml", mode="r", encoding="utf-8") as weapons_data_file:
    weapons_data = yaml.safe_load(weapons_data_file)

def get_weapon_data():
    return weapons_data
