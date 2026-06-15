from classes.Entities.Enemy.BaseEnemy import BaseEnemy
from classes.Entities.Enemy.BossEnemy import BossEnemy

class EnemyRegistry:
    @staticmethod
    def get_enemy_class(is_boss):
        if is_boss:
            return BossEnemy
        else:
            return BaseEnemy