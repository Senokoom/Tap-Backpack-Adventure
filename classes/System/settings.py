import yaml

with open('settings.yaml', mode="r", encoding="utf-8") as settings:
    settings = yaml.safe_load(settings)

max_cap_rare_item_chance = settings["math_settings"]["max_cap_rare_item_chance"]
