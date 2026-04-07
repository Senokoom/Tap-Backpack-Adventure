from classes.Item.Item import Item


class Weapon(Item):
    def __init__(self, name, rarity, height, width, stats, price, img=None, _type=None):
        super().__init__(name, rarity, height, width, price, stats, _type, img)
        _type = "Weapon"