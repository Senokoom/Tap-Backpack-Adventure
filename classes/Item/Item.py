class Item:
    def __init__(self, id, name, rarity, _type, height, width, price, img=None, stats=None):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.type = _type
        self.height = height
        self.width = width
        self.price = price
        self.img = img
        self.stats = stats
