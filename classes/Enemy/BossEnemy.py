from Enemy import Enemy

class BossEnemy(Enemy):
    def __init__(self, id, name, hp, resistance):
        super().__init__(id, name, hp, resistance, is_boss=True)