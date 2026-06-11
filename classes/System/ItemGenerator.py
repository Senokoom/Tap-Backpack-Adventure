from classes.Item.Armor import Armor
from classes.Item.Trinket import Trinket
from classes.Item.Weapon import Weapon
from classes.Item.Consumable import Consumable

from DataManagment.dataloader import weapon_data, prefix_data, suffix_data
from classes.System.settings  import Config
from math import floor
from random import randint, choice

class ItemGenerator:

    def __init__(self):
        pass

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
            merge_stats(stats_list), level_when_dropped, self.generate_item_price(final_parts)
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
                                                       merge_stats(stats_list), level_when_dropped, self.generate_item_price(final_parts))
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
            item_name += item_parts_dict[part]['name'][Config.language] + " "
        return item_name


    def generate_item_price(self, item_parts_dict):
        priced_parts = 0
        for part, value in item_parts_dict.items():
            priced_parts += Config.rarity_to_price[item_parts_dict[part]['rarity']]
        return priced_parts


    def apply_weights_bonus(self, bonus):
        bonus = bonus if bonus <= Config.max_cap_rare_item_chance else Config.max_cap_rare_item_chance
        bonus_buffer = 0
        final_weights = {}
        for key, weight in Config.default_rarity_weights.items():
            final_weights[key] = abs(Config.default_rarity_weights[key] + bonus_buffer - floor((Config.default_rarity_weights[key] + bonus_buffer) * bonus))
            bonus_buffer = floor((Config.default_rarity_weights[key] + bonus_buffer) * bonus)
        total = sum(final_weights.values())
        for key, weight in final_weights.items():
            final_weights[key] = round(final_weights[key]/total * 100)
        if sum(final_weights.values()) != 100:
            final_weights["common"] += 100 - sum(final_weights.values())
        return final_weights



    #Покачто будут только Weapon. Иначе я просто не успею закончить проект.
    def generate_weapon_item(self, player, level_when_dropped):
        return self.generate_item(player.stats["rare_item_chance"], [prefix_data, weapon_data, suffix_data], "weapon", level_when_dropped)




def merge_stats(stats_list):
    result_stats = {}

    for item_stats in stats_list:
        for stat_name, modifiers_list in item_stats.items():
            # На случай, если вдруг придёт одиночный dict, а не список
            if not isinstance(modifiers_list, list):
                modifiers_list = [modifiers_list]

            if stat_name not in result_stats:
                result_stats[stat_name] = []

            for modifier in modifiers_list:
                found_match = False
                for existing in result_stats[stat_name]:
                    if existing["type"] == modifier["type"]:
                        if modifier["type"] == "multiply":
                            existing["value"] *= modifier["value"]
                        elif modifier["type"] == "add":
                            existing["value"] += modifier["value"]
                        found_match = True
                        break  # ← Останавливаем поиск после слияния

                if not found_match:
                    # Копируем, чтобы не ломать исходные данные предмета
                    result_stats[stat_name].append(modifier.copy())

    return result_stats