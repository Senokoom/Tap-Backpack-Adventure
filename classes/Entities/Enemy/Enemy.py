
class Enemy:
    def __init__(self, id, name, hp, resistance, is_boss, level, price, xp, img=None):
        self.id = id
        self.name = name
        self.hp = hp
        self.current_hp = self.hp
        self.resistance = resistance
        self.is_boss = is_boss
        self.is_dead = False
        self.level = level
        self.price = price
        self.xp = xp
        self.image = img

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.has_died()

    def has_died(self):
        self.is_dead = True

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            hp=data['hp'],
            resistance=data['resistance'],
            is_boss=data['is_boss'],
            level=data['level'],
            price=data['price'],
            xp=data['xp'],
            img=data['image']
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "hp": self.hp,
            "resistance": self.resistance,
            "is_boss": self.is_boss,
            "level": self.level,
            "price": self.price,
            "xp": self.xp,
            "image": self.image
        }

    def __str__(self):
        return f"id = {self.id}\nname = {self.name}\nis_boss = {self.is_boss}\nresists = {self.resistance}"