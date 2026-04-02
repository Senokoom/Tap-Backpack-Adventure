from classes.Item.Item import Item


class Armor(Item):
    def __init__(self, id, name, rarity, _type, height, width, price, img=None, stats=None):
        super().__init__(id, name, rarity, height, width, price, _type, img, stats)
        _type = "Armor"