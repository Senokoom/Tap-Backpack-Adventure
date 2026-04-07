from classes.Item.Item import Item


class Consumable(Item):
    def __init__(self, name, rarity, height, width, price, uses, duration, _type=None, img=None, stats=None):
        super().__init__(name, rarity, height, width, price, stats, _type, img)
        self._type = "Consumable"
        self.uses = uses
        self.duration = duration


    def consume(self):
        if self.uses > 0:
            self.uses -= 1
        return self.stats, self.duration

