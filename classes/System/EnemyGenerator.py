from classes.Entities.Enemy.BaseEnemy import BaseEnemy
from classes.Entities.Enemy.BossEnemy import BossEnemy
from DataManagment.dataloader import enemy_data
from random import choice
from classes.System.settings import Config

class EnemyGenerator:
    def __init__(self):
        pass

    def spawn(self, is_boss, level):
        enemy_dict = choice(enemy_data)
        if is_boss:
            return self.spawn_boss_enemy(enemy_dict, level)
        else:
            return self.spawn_base_enemy(enemy_dict, level)


    def spawn_boss_enemy(self, enemy_dict, level):
        return BossEnemy(
            enemy_dict["id"],
            enemy_dict["name"][Config.language],
            enemy_dict["hp"],
            enemy_dict["resists"],
            True,
            level,
            enemy_dict["price"],
            enemy_dict["xp"]
        )

    def spawn_base_enemy(self, enemy_dict, level):
        return BaseEnemy(
            enemy_dict["id"],
            enemy_dict["name"][Config.language],
            enemy_dict["hp"],
            enemy_dict["resists"],
            False,
            level,
            enemy_dict["price"],
            enemy_dict["xp"]
        )
