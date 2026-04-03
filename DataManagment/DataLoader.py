import yaml

with open("data/weapons_en_ru.yaml", mode="r", encoding="utf-8") as weapons_data_file:
    weapons_data = yaml.safe_load(weapons_data_file)

language = "ru"


def get_weapon_data():
    return [
        weapons_data["weapon"],
        weapons_data["prefix"],
        weapons_data["suffix"],
    ]
