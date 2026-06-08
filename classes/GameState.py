from classes.Entities.Enemy.Enemy import Enemy
from classes.Entities.Player import Player
from classes.System.Calculator import Calculator
from classes.System.EnemyGenerator import EnemyGenerator
from classes.System.ItemGenerator import ItemGenerator
from classes.System.settings import Config


class GameState:
    def __init__(self, player: Player, calculator: Calculator, itemgenerator: ItemGenerator,enemygenerator: EnemyGenerator, current_enemy: Enemy, progression=1):
        self.player = player
        self.calculator = calculator
        self.itemgenerator = itemgenerator
        self.enemygenerator = enemygenerator
        self.current_enemy = current_enemy
        self.progression = progression
        self.pending_loot = []


    def spawn_enemy(self):
        if self.progression%Config.boss_frequency_value == 0:
            self.current_enemy = self.enemygenerator.spawn(True, 1+self.progression//Config.boss_frequency_value)
        else:
            self.current_enemy = self.enemygenerator.spawn(False, 1+self.progression//Config.boss_frequency_value)
        self.current_enemy.current_hp = self.calculator.get_max_hp_scaled(self.current_enemy)

    def handle_tap(self):
        if not self.current_enemy or self.current_enemy.is_dead:
            self.spawn_enemy()
        self.current_enemy.take_damage(self.calculator.get_damage(self.player, self.current_enemy))
        if self.current_enemy.is_dead:
            self.on_enemy_death()


    def on_enemy_death(self):
        self.player.xppoints += self.calculator.get_enemy_xp_drop(self.current_enemy, self.player)
        self.player.gold += self.calculator.get_gold_drop(self.current_enemy, self.player)
        #С каждого врага будет что-то дропаться
        print("Сгенерил оружие")
        # self.pending_loot.append(self.itemgenerator.generate_weapon_item(self.player, self.player.level))
        self.progression += 1
        self.spawn_enemy()

