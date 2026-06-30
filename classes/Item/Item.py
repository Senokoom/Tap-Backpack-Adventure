from classes.Item.ItemABC import ItemABC


class Item(ItemABC):
    def __init__(self, id, name, rarity, height, width, price, stats, level, _type=None, img=None):
        self.id = id
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

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            rarity=data['rarity'],
            height=data['height'],
            width=data['width'],
            price=data['price'],
            img=data['img'],
            stats=data['stats'],
            level=data['level']
        )

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "rarity": self.rarity,
            "_type": self._type,
            "height": self.height,
            "width": self.width,
            "price": self.price,
            "img": self.img,
            "stats": self.stats,
            "level": self.level
        }


    #ТУпо для дебага было
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

    def __str__(self):
        return f"{self.name}"

    def __lt__(self, other):
        return self.level < other.level

    def __eq__(self, other):
        return self.level == other.level
