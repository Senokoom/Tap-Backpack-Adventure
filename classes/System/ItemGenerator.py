from classes.Item.Armor import Armor
from classes.Item.Trinket import Trinket
from classes.Item.Weapon import Weapon
from classes.Item.Consumable import Consumable

from DataManagment.DataLoader import get_weapon_data, get_prefix_data, get_suffix_data
from settings import max_cap_rare_item_chance, language
from math import floor
from random import randint, choice

class ItemGenerator:

    def __init__(self):
        weapon_data = get_weapon_data()
        self.weapon_info = weapon_data
        self.rarity_weights = {
            "common": 60,
            "uncommon": 25,
            "rare": 10,
            "epic": 4,
            "legendary": 1
        }

    # Генерирует СТРОГО оружие
    def generate_item(self, bonus, item_info):
        """
        Написал эту хуйню сюда, чтоб не забыть что такое item_info :)
        Кстати, здравствуйте :))

        :param bonus: Бонус к шансу редкости
        :param item_info: Короче, это список(list) из prefix, item_type(либо weapon, armor, etc.), suffix. СТОРО В ЭТОМ ПОРЯДКЕ
        :return: новый Item
        """
        item_type_to_class = {
            "weapon": Weapon,
            "armor": Armor,
            "trinket": Trinket,
            "consumable": Consumable
        }
        chance_list = self.apply_weights_bonus(bonus)
        final_parts = {}
        final_rarity = 0
        for name_type in item_info:
            for name in name_type.keys():
                print(f"ВЫБИРАЮ: {name}")
                rarity_random_chance = randint(0, 100)
                rarity_random_chance_value = 0
                for rarity, rarity_value in reversed(chance_list.items()):
                    if (100 - rarity_random_chance) <= rarity_value:
                        rarity_random_chance_value = rarity
                        break
                rarity_random_chance_value = "common" if rarity_random_chance_value == 0 else rarity_random_chance_value
                final_rarity += (100-rarity_random_chance)
                print(f"ВОТ С ТАКОЙ РЕДКОСТЬЮ: {rarity_random_chance_value}")
                temp_possible_weapon_part_list = []
                for item_part in name_type[name]:
                    print(item_part)
                    if item_part["rarity"] == rarity_random_chance_value:
                        temp_possible_weapon_part_list.append(item_part)
                        print(f"{item_part['name'][language]} ДОБАВЛЕН В СПИСОК ВОЗМОЖНЫХ")
                final_parts[name] = choice(temp_possible_weapon_part_list)
                print(f" В ИТОГЕ ВЫБРАЛ {final_parts[list(final_parts)[-1]]['name'][language]}")
                print("--------------------------------------------------")
        print("--------------------------------")
        print("Финальное оружие")
        string = ''
        print(final_parts)
        for part, value in final_parts.items():
            string += final_parts[part]['name'][language] + " "
        print(string)
        for rarity, rarity_value in reversed(chance_list.items()):
            if (100 - final_rarity) <= rarity_value*len(final_parts):
                final_rarity = rarity
                break



    def apply_weights_bonus(self, bonus):
        bonus = bonus if bonus <= max_cap_rare_item_chance else max_cap_rare_item_chance
        bonus_buffer = 0
        final_weights = {}
        for key, weight in self.rarity_weights.items():
            final_weights[key] = abs(self.rarity_weights[key]+bonus_buffer-floor((self.rarity_weights[key]+bonus_buffer)*bonus))
            bonus_buffer = floor((self.rarity_weights[key] + bonus_buffer)*bonus)
        total = sum(final_weights.values())
        for key, weight in final_weights.items():
            final_weights[key] = round(final_weights[key]/total * 100)
        if sum(final_weights.values()) != 100:
            final_weights["common"] += 100 - sum(final_weights.values())
        return final_weights

    def merge_dicts_in_list(self, dict_list: list) -> list:
        result_list = []
        for dict in dict_list:
            print(dict)

debug = ItemGenerator()
# debug.generate_item(0.5, {
#     "prefix": get_prefix_data(),
#     "item": get_weapon_data(),
#     "suffix": get_suffix_data()})
debug.generate_item(0.5, [get_prefix_data(), get_weapon_data(), get_suffix_data()])