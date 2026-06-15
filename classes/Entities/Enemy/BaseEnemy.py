from classes.Entities.Enemy.Enemy import Enemy

class BaseEnemy(Enemy):
    is_boss = False

    def __init__(self, id, name, hp, resistance, is_boss, level, price, xp, img=None):
        super().__init__(id, name, hp, resistance, self.is_boss, level, price, xp, img)
