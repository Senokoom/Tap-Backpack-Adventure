from random import randint

from classes.System.ItemGenerator import ItemGenerator
from classes.System.settings import (player_progression_value,
                                     item_add_progression_value,
                                     item_multiply_progression_value,
                                     item_price_progression_value,
                                     enemy_hp_progression_value,
                                     economy_gold_progression_value,
                                     economy_price_progression_value)


class Calculator:
    def __init__(self):
        pass

    def get_damage(self, player, enemy):
        """
        Короче, это ебать огромная функция наверн будет. Потому что она должна будет учитывать оружия, бафы и все
        множители и даже блять резисты врага и выдавать чисто число. Ебать фукнция огромная будет, я вахуи
        """
        pass



    def get_current_player_stats(self, player):
        pass


    def get_max_hp_scaled(self, enemy):
        enemy.current_hp *= (enemy_hp_progression_value ** enemy.level)
        return


    def get_gold_drop(self, enemy, player):
        gold_dropped = 0
        if enemy.is_boss:
            gold_dropped *= ((economy_gold_progression_value ** enemy.price)*(randint(2, 4)))*player.stats["gold_drop"]
        else:
            gold_dropped *= (economy_gold_progression_value ** enemy.price)*player.stats["gold_drop"]
        return gold_dropped


    def get_item_price(self, item):
        item.current_price *= (item_price_progression_value ** item.level)
        return


    def get_item_stat(self, item):
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
        item.current_stats = new_stats
        return



    def get_progression_multiplier(self, player):
        pass



item_generator_debug = ItemGenerator()
calculator_debug = Calculator()
weapon = item_generator_debug.debug_generate_weapon_item(0.2, 5000)
print(weapon.get_info())
print(calculator_debug.get_item_stat(weapon))
