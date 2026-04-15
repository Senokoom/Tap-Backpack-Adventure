from classes.Item.Item import Item


class Trinket(Item):
    def __init__(self, name, rarity, height, width, stats, level, price,  img=None, _type=None):
        super().__init__(name, rarity, height, width, price, stats, level, _type, img)
        self._type = "Trinket"