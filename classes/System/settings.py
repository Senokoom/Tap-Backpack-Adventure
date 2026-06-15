from pathlib import Path
import yaml


class Config:
    project_data_dir = Path(__file__).resolve().parent.parent / "System"
    with open(project_data_dir / 'settings.yaml', mode="r", encoding="utf-8") as settings:
        settings = yaml.safe_load(settings)


    #Item Generation Settings
    max_cap_rare_item_chance = settings["item_generation_settings"]["max_cap_rare_item_chance"]
    rarity_to_price = settings["item_generation_settings"]["rarity_to_price"]
    default_rarity_weights = settings["item_generation_settings"]["default_rarity_weights"]

    #Item Progression and Player thingy
    player_progression_value = settings["progression_settings"]["player"]["base_growth"] # не использую пока
    item_add_progression_value = settings["progression_settings"]["item"]["add_growth"]
    item_multiply_progression_value = settings["progression_settings"]["item"]["multiply_growth"]

    #Economy Settings
    item_price_progression_value = settings["progression_settings"]["item"]["price_growth"]
    economy_gold_progression_value = settings["progression_settings"]["economy"]["gold_growth"]
    economy_price_progression_value = settings["progression_settings"]["economy"]["price_growth"]

    #Enemy Settings
    enemy_hp_progression_value = settings["progression_settings"]["enemy"]["hp_growth"]
    boss_hp_multiplier_value = settings["progression_settings"]["enemy"]["boss_hp_multiplier"]
    boss_frequency_value = settings["progression_settings"]["enemy"]["boss_frequency"]
    xp_drop_multiplier_value = settings["progression_settings"]["enemy"]["xp_drop_multiplier"]
    boss_xp_drop_multiplier_value = settings["progression_settings"]["enemy"]["boss_xp_drop_multiplier"]
    boss_price_multiplier_value = settings["progression_settings"]["enemy"]["boss_price_multiplier"]

    #Game Settings
    language = settings["game_settings"]["language"]

    #Save Settings
    save_dir = settings["save_settings"]["save_dir"]
    save_filename = settings["save_settings"]["save_filename"]


    #New Game Settings
    new_game_player_stats = settings["new_game_settings"]["player"]
    new_game_active_inventory = settings["new_game_settings"]["active_inventory"]
    new_game_backpack_inventory = settings["new_game_settings"]["backpack_inventory"]