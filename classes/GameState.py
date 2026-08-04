from classes.Entities.Enemy.Enemy import Enemy
from classes.Entities.Player import Player
from classes.Item.Item import Item
from classes.System.Calculator import Calculator
from classes.System.EnemyGenerator import EnemyGenerator
from classes.System.ItemGenerator import ItemGenerator
from classes.System.enemy_registry import EnemyRegistry
from classes.System.item_registry import ItemRegistry
from classes.System.settings import Config

from random import randint

class GameState:
    def __init__(self, player: Player, current_enemy: Enemy = None, progression=1,
                 pending_loot=None):
        if pending_loot is None:
            pending_loot = []
        self.player = player
        self.calculator = Calculator()
        self.itemgenerator = ItemGenerator()
        self.enemygenerator = EnemyGenerator()
        self.current_enemy = current_enemy
        self.progression = progression
        self.pending_loot = pending_loot
        self.last_damage = 0

    def spawn_enemy(self):
        if self.progression%Config.boss_frequency_value == 0:
            self.current_enemy = self.enemygenerator.spawn(True, 1+self.progression//Config.boss_frequency_value)
        else:
            self.current_enemy = self.enemygenerator.spawn(False, 1+self.progression//Config.boss_frequency_value)
        self.current_enemy.current_hp = self.calculator.get_max_hp_scaled(self.current_enemy)

    def handle_tap(self):
        if not self.current_enemy or self.current_enemy.is_dead:
            self.spawn_enemy()
        self.last_damage = self.calculator.get_damage(self.player, self.current_enemy)
        self.current_enemy.take_damage(self.last_damage)
        if self.current_enemy.is_dead:
            self.on_enemy_death()


    def on_enemy_death(self):
        self.player.xppoints += self.calculator.get_enemy_xp_drop(self.current_enemy, self.player)
        self.player.gold += self.calculator.get_gold_drop(self.current_enemy, self.player)
        if randint(0, 100) <= self.player.stats["item_drop"] or self.current_enemy.is_boss:
            print(weapon := self.itemgenerator.generate_weapon_item(self.player, self.player.level).get_info())
            self.pending_loot.append(weapon)
        if self.player.xppoints >= self.calculator.get_xp_for_next_level(self.player):
            self.player.level += 1
            self.player.skill_point += 1
        self.progression += 1
        self.spawn_enemy()

    def get_enemy_max_health(self):
        if self.current_enemy is None:
            self.spawn_enemy()
        return self.calculator.get_max_hp_scaled(self.current_enemy)

    def get_enemy_current_hp(self):
        return self.current_enemy.current_hp

    def get_player_current_stats(self):
        return self.calculator.get_current_player_stats(self.player)

    def get_player_base_stats(self):
        return self.player.stats

    def get_player_name(self):
        return self.player.name

    def get_player_last_damage(self):
        return self.last_damage

    def get_player_skill_points(self):
        return self.player.skill_point

    def get_player_gold(self):
        return self.player.gold

    def get_player_xp(self):
        return self.player.xppoints

    def get_player_level(self):
        return self.player.level

    def get_enemy_level(self):
        return self.current_enemy.level

    def get_enemy_name(self):
        return self.current_enemy.name

    def get_active_inventory_width_height(self):
        return self.player.ActiveInventory.width, self.player.ActiveInventory.height

    def get_player_level_up(self, skill):
        self.player.skill_levelup(skill, Config.player_level_up_values[skill])

    def get_active_inventory_ui_data(self):
        ui_matrix = []
        for y in range(self.player.ActiveInventory.height):
            row = []
            for x in range(self.player.ActiveInventory.width):
                cell = self.player.ActiveInventory.inventory_matrix[y][x]
                if cell.item:
                    row.append({
                        "name": cell.item.name,
                        "rarity": cell.item.rarity,
                        "stats": cell.item.stats
                    })
                else:
                    row.append(None)
            ui_matrix.append(row)
        return ui_matrix

    def get_backpack_inventory_ui_data(self):
        ui_matrix = []
        for y in range(self.player.BackpackInventory.height):
            row = []
            for x in range(self.player.BackpackInventory.width):
                cell = self.player.BackpackInventory.inventory_matrix[y][x]
                if cell.item:
                    row.append({
                        "name": cell.item.name,
                        "rarity": cell.item.rarity,
                        "stats": cell.item.stats
                    })
                else:
                    row.append(None)
            ui_matrix.append(row)
        return ui_matrix


##___________________________ЧИСТО СОХРАНЕНИЕ_______________________

    def to_dict(self):
        dict = {
            "player": self.player.to_dict(),
            "current_enemy": None if not self.current_enemy else self.current_enemy.to_dict(),
            "progression": self.progression,
            "pending_loot": None if not self.pending_loot else [item.to_dict() for item in self.pending_loot]
        }
        return dict

    @classmethod
    def from_dict(cls, data):
        _pending_loot = []
        if data["pending_loot"] is not None:
            for item in data['pending_loot']:
                _pending_loot.append(ItemRegistry.get_item_class(item['_type']).from_dict(item))
        return GameState(
            player=Player.from_dict(data['player']),
            current_enemy=None if not data['current_enemy'] else EnemyRegistry.get_enemy_class(data['current_enemy']['is_boss']).from_dict(data['current_enemy']),
            progression=data['progression'],
            pending_loot=_pending_loot
        )