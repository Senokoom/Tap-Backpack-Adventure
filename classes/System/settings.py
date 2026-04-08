import yaml

with open('settings.yaml', mode="r", encoding="utf-8") as settings:
    settings = yaml.safe_load(settings)

max_cap_rare_item_chance = settings["math_settings"]["max_cap_rare_item_chance"]
rarity_to_price = settings["math_settings"]["rarity_to_price"]
default_rarity_weights = settings["math_settings"]["default_rarity_weights"]


language = settings["settings"]["language"]
