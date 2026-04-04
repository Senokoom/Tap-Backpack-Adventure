from classes.Item.Armor import Armor
from classes.Item.Trinket import Trinket
from classes.Item.Weapon import Weapon
from classes.Item.Consumable import Consumable
from DataManagment.DataLoader import get_weapon_data
from settings import max_cap_rare_item_chance
from math import floor

class ItemGenerator:

    def __init__(self):
        weapon_data = get_weapon_data()
        self.weapon, self.suffix, self.prefix = weapon_data["weapon"], weapon_data["suffix"], weapon_data["prefix"]
        self.rarity_weights = {
            "common": 60,
            "uncommon": 25,
            "rare": 10,
            "epic": 4,
            "legendary": 1
        }

    # Генерирует СТРОГО оружие
    def generate_weapon(self, weapon_info) -> Weapon:
        weapon_name, weapon_prefix, weapon_suffix = weapon_info["weapon"], weapon_info["prefix"], weapon_info["suffix"]

    def create_weighted_lists(self, bonus):
        for key, value in self.apply_weights_bonus(bonus):
            pass

    def apply_weights_bonus(self, bonus):
        bonus = bonus if bonus <= max_cap_rare_item_chance else max_cap_rare_item_chance
        bonus_buffer = 0
        final_weights = {}
        for key, weight in self.rarity_weights.items():
            final_weights[key] = abs(self.rarity_weights[key]+bonus_buffer-floor((self.rarity_weights[key]+bonus_buffer)*bonus))
            bonus_buffer = floor((self.rarity_weights[key] + bonus_buffer)*bonus)
            print(final_weights)
        return final_weights
