class Enemy:
    def __init__(self, id, name, hp, resistance, is_boss, level, price, img=None):
        self.id = id
        self.name = name
        self.hp = hp
        self.current_hp = self.hp
        self.resistance = resistance
        self.is_boss = is_boss
        self.is_dead = False
        self.level = level
        self.price = price
        self.image = img

    def take_damage(self, damage):
        # {
        #     "physical_damage": physical_damage,
        #     "fire_damage": fire_damage,
        #     "ice_damage": ice_damage,
        #     "lightning_damage": lightning_damage,
        #     "emotional_damage": emotional_damage,
        #     "critical_damage": critical_damage
        # }
        final_damage = 0
        for key, value in damage.items():
            final_damage += (value if key not in self.resistance else (1-self.resistance[key])*value)
        self.hp -= final_damage
        if self.hp <= 0:
            self.has_died()

    def has_died(self):
        self.is_dead = True
        return