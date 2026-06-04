from random import randint
from classes.System.ItemGenerator import ItemGenerator, merge_stats
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
        player.current_stats = self.get_current_player_stats(player)
        enemy.take_damage(player.current_stats)

    def get_active_weapons_stats(self, player):
        combined_item_stats = []
        for item in player.ActiveInventory.item_list:
            combined_item_stats.append(self.get_item_stat(item))
        return merge_stats(combined_item_stats)

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
        return enemy.hp * (enemy_hp_progression_value ** enemy.level)

    def get_gold_drop(self, enemy, player):
        if enemy.is_boss:
            return ((economy_gold_progression_value ** enemy.price)*(randint(2, 4)))*player.stats["gold_drop"]
        else:
            return (economy_gold_progression_value ** enemy.price)*player.stats["gold_drop"]

    def get_item_price(self, item):
        return item.price * (item_price_progression_value ** item.level)
    
    def get_economy_price(self, item):
        return item.price * (economy_price_progression_value ** item.level)

    def get_item_stat(self, item):
        new_stats = {}
        for current_stat in item.stats:
            for value in item.stats[current_stat]:
                if not current_stat in new_stats:
                    new_stats[current_stat] = []
                if value['type'] == 'add':
                    new_stats[current_stat].append({"value": value['value'] * (item_add_progression_value ** item.level), "type": 'add'})
                elif value['type'] == 'multiply':
                    new_stats[current_stat].append({"value": value['value'] * (item_multiply_progression_value ** item.level), "type": 'multiply'})
        return new_stats



### ТУТ ВНИЗУ КОД КОТОРЫЙ Я ИСПОЛЬЗОВАЛ ДЛЯ ДЕБАГА ЭТОГО КЛАССА. ПАМАГИТИ, Я БЕРЕБОРЩИЛ С РАЗМЕРОМ ПРОЕКТА......

# # debugging :)
# from classes.Entities.Player import Player
# from classes.Inventory import ActiveInventory, BackpackInventory, Inventory  # или там, где у тебя лежит Inventory
#
# # 1. Создаём инвентари (укажи свои размеры сетки)
# # ActiveInventory обычно маленький (например, 3x3 или 4x4 для экипировки)
# active_inv = ActiveInventory.ActiveInventory(width=4, height=4)
#
# # BackpackInventory — основной рюкзак (например, 8x6 как в Backpack Hero)
# backpack_inv = BackpackInventory.BackpackInventory(width=8, height=6)
#
# # 2. Создаём игрока с минимальными тестовыми данными
# debug_player = Player(
#     id=1,
#     name="TestHero",
#     xppoints=0,
#     gold=100,
#     level=1,
#     skill_point=3,
#     ActiveInventory=active_inv,
#     BackpackInventory=backpack_inv,
#     last_time_online=0  # или time.time(), если используешь модуль time
# )
#
# # 3. Быстрая проверка
# print(f"Игрок: {debug_player.name}, Золото: {debug_player.gold}")
# print(f"Статы по умолчанию: {debug_player.stats}")
# print(f"Размер рюкзака: {debug_player.BackpackInventory.width}x{debug_player.BackpackInventory.height}")
#
#
#
# item_generator_debug = ItemGenerator()
# calculator_debug = Calculator()
# weapon = item_generator_debug.debug_generate_weapon_item(0.2, 100)
# weapon1 = item_generator_debug.debug_generate_weapon_item(0.2, 100)
# print(f"Информация о предмете: {weapon.get_info()}")
#
# print(f"Результат добавления предмета в ActiveInventory: {debug_player.ActiveInventory.add_item(weapon, 1, 0)}")
# print(f"Результат добавления ВТОРОГО предмета в ActiveInventory: {debug_player.ActiveInventory.add_item(weapon1, 0, 0)}")
#
# print(f"Сам инвентарь ниже\n{debug_player.ActiveInventory.inventory_to_string()}")
# print(f"Предметы в инвенторе: {debug_player.ActiveInventory.item_list_to_string()}")
# # print(calculator_debug.get_item_stat(weapon))
# # print(weapon.get_info())
# # weapon.current_stats = calculator_debug.get_item_stat(weapon)
# # print(weapon.get_info())
# print(calculator_debug.get_current_player_stats(debug_player))
#
#
#
# # ВРАГ ДЛЯ ДЕБАГА
# from classes.Entities.Enemy.BaseEnemy import BaseEnemy
# debug_enemy = BaseEnemy(
#     id=1,
#     name="Debug Slime",
#     hp=100,
#     resistance={
#         "physical_damage": 0.1,   # 10% сопротивления
#         "fire_damage": 0.3,       # 30% сопротивления
#         "ice_damage": 0.0,        # 0%
#         "lightning_damage": 0.5,  # 50%
#         "emotional_damage": 0.2,  # 20%
#         "critical_damage": 0.0    # обычно крит не режется, но оставил для структуры
#     },
#     level=101,
#     price=15
# )
#
# # Тестовый урон
# test_damage = {
#     "physical_damage": 50,
#     "fire_damage": 20,
#     "lightning_damage": 10,
#     "emotional_damage": 5
# }
# debug_enemy.current_hp = calculator_debug.get_max_hp_scaled(debug_enemy)
#
# print(f"HP до удара: {debug_enemy.current_hp}")
# calculator_debug.get_damage(debug_player, debug_enemy)
# calculator_debug.get_damage(debug_player, debug_enemy)
# calculator_debug.get_damage(debug_player, debug_enemy)
# calculator_debug.get_damage(debug_player, debug_enemy)
# calculator_debug.get_damage(debug_player, debug_enemy)
# print(f"HP после удара: {debug_enemy.current_hp}")
# print(f"Враг мёртв? {debug_enemy.is_dead}")