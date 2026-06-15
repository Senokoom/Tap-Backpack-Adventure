from classes.Item.Item import Item


class Armor(Item):
    def __init__(self, id, name, rarity, height, width, stats, level, price,  img=None, _type=None):
        super().__init__(id, name, rarity, height, width, price, stats, level, _type, img)
        self._type = "Armor"