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

        #будет высчитывать урон от всех статов, что есть, и отправлять в виде словарика(уже потом будут всякие дебафы идти и т.д.
        physical_damage = self.stats["physical_damage"]
        fire_damage = self.stats["fire_damage"]
        ice_damage = self.stats["ice_damage"]
        lightning_damage = self.stats["lightning_damage"]
        emotional_damage = self.stats["emotional_damage"]
        critical_damage = (physical_damage + fire_damage + ice_damage + lightning_damage + emotional_damage)* (self.stats["critical_damage"] if random.random() <= self.stats["critical_damage_chance"] else 0)
        return{
            "physical_damage": physical_damage,
            "fire_damage": fire_damage,
            "ice_damage": ice_damage,
            "lightning_damage": lightning_damage,
            "emotional_damage": emotional_damage,
            "critical_damage": critical_damage
        }
        """

        pass

    def get_active_weapons_stats(self, player):
        combined_item_stats = []

        for item in player.ActiveInventory.item_list:
            combined_item_stats.append(self.get_item_stat(item))
        for item in combined_item_stats:
            pass



    def get_current_player_stats(self, player):
        pass


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



    #Чтобы работало нормально в 100% случаев, так же надо будет переписать merg
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



    def get_progression_multiplier(self, player):
        pass



# debug_player.py
from classes.Entities.Player import Player
from classes.Inventory import ActiveInventory, BackpackInventory, Inventory  # или там, где у тебя лежит Inventory

# 1. Создаём инвентари (укажи свои размеры сетки)
# ActiveInventory обычно маленький (например, 3x3 или 4x4 для экипировки)
active_inv = ActiveInventory.ActiveInventory(width=6, height=6)

# BackpackInventory — основной рюкзак (например, 8x6 как в Backpack Hero)
backpack_inv = BackpackInventory.BackpackInventory(width=8, height=6)

# 2. Создаём игрока с минимальными тестовыми данными
debug_player = Player(
    id=1,
    name="TestHero",
    xppoints=0,
    gold=100,
    level=1,
    skill_point=3,
    ActiveInventory=active_inv,
    BackpackInventory=backpack_inv,
    last_time_online=0  # или time.time(), если используешь модуль time
)

# 3. Быстрая проверка
print(f"Игрок: {debug_player.name}, Золото: {debug_player.gold}")
print(f"Статы по умолчанию: {debug_player.stats}")
print(f"Размер рюкзака: {debug_player.BackpackInventory.width}x{debug_player.BackpackInventory.height}")



item_generator_debug = ItemGenerator()
calculator_debug = Calculator()
weapon = item_generator_debug.debug_generate_weapon_item(0.2, 5)
print(f"Информация о предмете: {weapon.get_info()}")

print(f"Результат добавления предмета в ActiveInventory: {debug_player.ActiveInventory.add_item(weapon, 4, 4)}")

print(f"Сам инвентарь ниже\n{debug_player.ActiveInventory.inventory_to_string()}")
print(f"Предметы в инвенторе: {debug_player.ActiveInventory.item_list_to_string()}")
# print(calculator_debug.get_item_stat(weapon))
# print(weapon.get_info())
# weapon.current_stats = calculator_debug.get_item_stat(weapon)
# print(weapon.get_info())
calculator_debug.get_active_weapons_stats(debug_player)
