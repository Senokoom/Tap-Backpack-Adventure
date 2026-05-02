from classes.Item.Item import Item
from classes.System.ItemGenerator import ItemGenerator
from classes.System.settings import (player_progression_value,
                                     item_add_progression_value,
                                     item_multiply_progression_value,
                                     enemy_hp_progression_value,
                                     economy_gold_progression_value,
                                     economy_price_progression_value)


class Calculator:
    progression_level = 1
    def __init__(self):
        pass

    def get_damage(self, player, enemy):
        """
        Короче, это ебать огромная функция наверн будет. Потому что она должна будет учитывать оружия, бафы и все
        множители и даже блять резисты врага и выдавать чисто число. Ебать фукнция огромная будет, я вахуи
        """
        pass

    def get_max_hp_scaled(self, enemy):
        pass

    def get_gold_drop(self, enemy, player):
        pass

    def get_item_value(self, item):
        pass

    def get_item_stat(self, item: Item):
        new_stats = {}
        for current_stat in item.stats:
            for value in item.stats[current_stat]:
                if not current_stat in new_stats:
                    new_stats[current_stat] = []
                if value['type'] == 'add':
                    value['value'] *= (item_add_progression_value ** item.level)
                    new_stats[current_stat].append(value)
                elif value['type'] == 'multiply':
                    value['value'] *= (item_multiply_progression_value ** item.level)
                    new_stats[current_stat].append(value)
        return new_stats



    def get_progression_multiplier(self, player):
        pass



item_generator_debug = ItemGenerator()
calculator_debug = Calculator()
weapon = item_generator_debug.debug_generate_weapon_item(0.2, 5000)
print(weapon.get_info())
print(calculator_debug.get_item_stat(weapon))
