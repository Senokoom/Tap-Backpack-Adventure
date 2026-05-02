from classes.Item.Armor import Armor
from classes.Item.Trinket import Trinket
from classes.Item.Weapon import Weapon
from classes.Item.Consumable import Consumable

from DataManagment.dataloader import get_weapon_data, get_prefix_data, get_suffix_data
from settings import max_cap_rare_item_chance, language, default_rarity_weights, rarity_to_price
from math import floor
from random import randint, choice

class ItemGenerator:

    def __init__(self):
        self.rarity_weights = default_rarity_weights
        self.rarity_to_price = rarity_to_price

    # Генерирует любой Айтем(по идее)
    def generate_item(self, bonus, item_info, item_type, level_when_dropped):
        """
        Написал эту хуйню сюда, чтоб не забыть что такое item_info :)
        Кстати, здравствуйте :))

        :param level_when_dropped: когда дропнулся
        :param item_type: че генерю
        :param bonus: Бонус к шансу редкости
        :param item_info: Короче, это список(list) из prefix, item_type(либо weapon, armor, etc.), suffix. СТОРО В ЭТОМ ПОРЯДКЕ
        :return: новый Item
        """
        final_parts = {}
        for name_type in item_info:
            for name in name_type.keys():
                rarity_random_chance = randint(0, 100)
                rarity_random_chance_value = 0
                for rarity, rarity_value in reversed(self.apply_weights_bonus(bonus).items()):
                    if (100 - rarity_random_chance) <= rarity_value:
                        rarity_random_chance_value = rarity
                        break
                rarity_random_chance_value = "common" if rarity_random_chance_value == 0 else rarity_random_chance_value
                temp_possible_weapon_part_list = []
                for item_part in name_type[name]:
                    if item_part["rarity"] == rarity_random_chance_value:
                        temp_possible_weapon_part_list.append(item_part)
                final_parts[name] = choice(temp_possible_weapon_part_list)
        stats_list = []
        for part, value in final_parts.items():
            stats_list.append(final_parts[part]['stats'])
        if item_type == Consumable:
            return self.generate_consumable(final_parts, stats_list, level_when_dropped)
        else:
            return self.generate_equipment(final_parts, item_type, stats_list, level_when_dropped)


    def generate_consumable(self, final_parts, stats_list, level_when_dropped):
        result_consumable = Consumable(
            self.generate_item_name(final_parts), self.generate_item_rarity(final_parts),
            final_parts["consumable"]["size"]["height"], final_parts["consumable"]["size"]["width"],
            final_parts["consumable"]["uses"], final_parts["consumable"]["duration"],
            self.merge_stats(stats_list), level_when_dropped ,self.generate_item_price(final_parts)
        )
        return result_consumable

    def generate_equipment(self, final_parts, item_type, stats_list, level_when_dropped):
        item_type_mapping = {
            "weapon": Weapon,
            "armor": Armor,
            "trinket": Trinket
        }
        result_item = item_type_mapping[item_type](self.generate_item_name(final_parts), self.generate_item_rarity(final_parts),
                                                       final_parts[item_type]["size"]["height"],
                                                       final_parts[item_type]["size"]["width"],
                                                       self.merge_stats(stats_list), level_when_dropped, self.generate_item_price(final_parts))
        return result_item




    def generate_item_rarity(self, item_parts_dict):
        parts_rarity = []
        weights_map = {
            "common": 0,
            "uncommon": 1,
            "rare": 2,
            "epic": 3,
            "legendary": 4
        }
        for part, value in item_parts_dict.items():
            parts_rarity.append(weights_map[item_parts_dict[part]['rarity']])
        return list(weights_map.keys())[round(sum(parts_rarity)/len(parts_rarity))]


    def generate_item_name(self, item_parts_dict):
        item_name = ''
        for part, value in item_parts_dict.items():
            item_name += item_parts_dict[part]['name'][language] + " "
        return item_name


    def generate_item_price(self, item_parts_dict):
        priced_parts = 0
        for part, value in item_parts_dict.items():
            priced_parts += self.rarity_to_price[item_parts_dict[part]['rarity']]
        return priced_parts


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


    def merge_stats(self, stats_list):
        result_stats = {}
        for stat in stats_list:
            for part, value in stat.items():
                if part in result_stats.keys():
                    for i in range(len(result_stats[part])):
                        if result_stats[part][i]["type"] != stat[part]["type"]:
                            result_stats[part].append(stat[part])
                        else:
                            if result_stats[part][i]["type"] == "multiply":
                                result_stats[part][i]["value"] *= stat[part]["value"]
                            elif result_stats[part][i]["type"] == "add":
                                result_stats[part][i]["value"] += stat[part]["value"]
                result_stats[part] = [stat[part]]
        return result_stats


    def debug_generate_weapon_item(self, bonus, level_when_dropped):
        return self.generate_item(bonus, [get_prefix_data(), get_weapon_data(), get_suffix_data()], "weapon", level_when_dropped)