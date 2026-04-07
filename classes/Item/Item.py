class Item:
    def __init__(self, name, rarity, height, width, price, _type=None, img=None, stats=None):
        self.name = name
        self.rarity = rarity
        self.type = _type
        self.height = height
        self.width = width
        self.price = price
        self.img = img
        self.stats = stats

    def get_info(self):
        return {
            "name": self.name,
            "rarity": self.rarity,
            "type": self.type,
            "height": self.height,
            "width": self.width,
            "stats": self.stats,
            "price": self.price
        }