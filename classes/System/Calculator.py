from numpy import random
from classes.System.ItemGenerator import ItemGenerator
from classes.System.settings import Config


class Calculator:
    def __init__(self):
        pass

    def get_damage(self, player, enemy):
        current_player_stats = self.get_current_player_stats(player)
        resistances = enemy.resistance
        final_damage = 0
        critical_strike = {
            "critical_damage_chance": current_player_stats["critical_damage_chance"],
            "critical_damage": current_player_stats["critical_damage"]
        }
        dealing_damage_stats = {
            "physical_damage": current_player_stats["physical_damage"],
            "fire_damage": current_player_stats["fire_damage"],
            "ice_damage": current_player_stats["ice_damage"],
            "lightning_damage": current_player_stats["lightning_damage"],
            "emotional_damage": current_player_stats["emotional_damage"]
        }
        for key, value in dealing_damage_stats.items():
            final_damage += (value if key not in resistances.keys() else (1 - resistances[key]) * value)
        final_damage += final_damage * (
            critical_strike["critical_damage"] if random.random() <= critical_strike["critical_damage_chance"] else 0)
        return final_damage

    def get_active_weapons_stats(self, player):
        combined_item_stats = []
        for item in player.ActiveInventory.item_list:
            combined_item_stats.append(self.get_item_stat(item))
        return ItemGenerator.merge_stats(combined_item_stats)

    # получаю их тут применяя бафы с оружия к player базовым статам
    def get_current_player_stats(self, player):
        base_stats = player.stats.copy()
        if len(player.ActiveInventory.item_list) != 0:
            weapon_stats = self.get_active_weapons_stats(player)
        else:
            return base_stats
        return self.apply_stats_to_stats(base_stats, weapon_stats)

    def apply_stats_to_stats(self, base_stats, applied_stats):
        values_to_add = {}
        values_to_multiply = {}
        for item, value in applied_stats.items():
            for stat in applied_stats[item]:
                if stat["type"] == "add":
                    values_to_add[item] = stat["value"]
                elif stat["type"] == "multiply":
                    values_to_multiply[item] = stat["value"]
        for stat, value in values_to_add.items():
            base_stats[stat] += value
        for stat, value in values_to_multiply.items():
            base_stats[stat] *= value
        return base_stats

    def get_max_hp_scaled(self, enemy):
        if enemy.is_boss:
            return (enemy.hp * (Config.enemy_hp_progression_value ** enemy.level)) * Config.boss_hp_multiplier_value
        else:
            return enemy.hp * (Config.enemy_hp_progression_value ** enemy.level)


    def get_gold_drop(self, enemy, player):
        if enemy.is_boss:
            return ((enemy.price * (Config.economy_gold_progression_value ** enemy.level)) * Config.boss_price_multiplier_value)*player.stats["gold_drop"]
        else:
            return (enemy.price * (Config.economy_gold_progression_value ** enemy.level))*player.stats["gold_drop"]


    def get_enemy_xp_drop(self, enemy, player):
        if enemy.is_boss:
            return ((enemy.xp * (Config.xp_drop_multiplier_value ** enemy.level))*Config.boss_xp_drop_multiplier_value) * player.stats["xp_drop"]
        else:
            return (enemy.xp * (Config.xp_drop_multiplier_value ** enemy.level))*player.stats["xp_drop"]


    def get_item_price(self, item):
        return item.price * (Config.item_price_progression_value ** item.level)
    
    def get_economy_price(self, item, economy_price_progression_value):
        return item.price * (economy_price_progression_value ** item.level)

    def get_item_stat(self, item):
        new_stats = {}
        for current_stat in item.stats:
            for value in item.stats[current_stat]:
                if not current_stat in new_stats:
                    new_stats[current_stat] = []
                if value['type'] == 'add':
                    new_stats[current_stat].append({"value": value['value'] * (Config.item_add_progression_value ** item.level), "type": 'add'})
                elif value['type'] == 'multiply':
                    new_stats[current_stat].append({"value": value['value'] * (Config.item_multiply_progression_value ** item.level), "type": 'multiply'})
        return new_stats