import yaml

with open('settings.yaml', mode="r", encoding="utf-8") as settings:
    settings = yaml.safe_load(settings)


#Item Generation Settings
max_cap_rare_item_chance = settings["item_generation_settings"]["max_cap_rare_item_chance"]
rarity_to_price = settings["item_generation_settings"]["rarity_to_price"]
default_rarity_weights = settings["item_generation_settings"]["default_rarity_weights"]


#Progression Settings
player_progression_value = settings["progression_settings"]["player"]["base_growth"]
item_add_progression_value = settings["progression_settings"]["item"]["add_growth"]
item_multiply_progression_value = settings["progression_settings"]["item"]["multiply_growth"]
item_price_progression_value = settings["progression_settings"]["item"]["price_growth"]
enemy_hp_progression_value = settings["progression_settings"]["enemy"]["hp_growth"]
economy_gold_progression_value = settings["progression_settings"]["economy"]["gold_growth"]
economy_price_progression_value = settings["progression_settings"]["economy"]["price_growth"]


#Game Settings
language = settings["game_settings"]["language"]
