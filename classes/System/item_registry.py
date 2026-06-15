
from classes.Item.Armor import Armor
from classes.Item.Consumable import Consumable
from classes.Item.Trinket import Trinket
from classes.Item.Weapon import Weapon


class ItemRegistry:
    @staticmethod
    def get_item_class(_type):
        ITEM_DATA_MAP = {
            "Consumable": Consumable,
            "Weapon": Weapon,
            "Armor": Armor,
            "Trinket": Trinket
        }
        return ITEM_DATA_MAP[_type]

