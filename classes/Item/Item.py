class Item:
    def __init__(self, name, rarity, height, width, price, stats, level, _type=None, img=None):
        self.name = name
        self.rarity = rarity
        self._type = _type
        self.height = height
        self.width = width
        self.price = price
        self.img = img
        self.stats = stats
        self.level = level
        self.current_stats = self.stats
        self.current_price = self.price

    def get_info(self):
        return {
            "name": self.name,
            "rarity": self.rarity,
            "level": self.level,
            "type": self._type,
            "height": self.height,
            "width": self.width,
            "stats": self.current_stats,
            "price": self.current_price
        }