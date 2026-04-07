from classes.Item.Item import Item


class Armor(Item):
    def __init__(self, name, rarity, height, width, price, img=None, stats=None):
        super().__init__(name, rarity, height, width, price, img, stats)
        _type = "Armor"