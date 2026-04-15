from Enemy import Enemy

class BaseEnemy(Enemy):
    def __init__(self, id, name, hp, resistance):
        super().__init__(id, name, hp, resistance, is_boss=False)