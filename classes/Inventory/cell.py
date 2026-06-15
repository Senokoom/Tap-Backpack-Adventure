from classes.Item.Item import Item
from classes.System.item_registry import ItemRegistry


class Cell:
    #это будет клеткой инвентаря(любого получается)
    item = None
    is_origin = False

    def __init__(self, item = None, is_origin = False, is_locked = True):
        self.item = item
        self.is_origin = is_origin
        self.is_locked = is_locked

    def to_string(self):
        result = ""
        if self.item is not None:
            result += f"{"0 " if self.is_origin and self.item is not None else "X " }"
        elif self.is_locked:
            result += f"U "
        else:
            result += f". "
        return result

    def to_dict(self):
        return {
            "item": None if not self.item else self.item.to_dict(),
            "is_origin": self.is_origin,
            "is_locked": self.is_locked
        }

    @classmethod
    def from_dict(cls, data):
        return Cell(
            item=None if data['item'] is None else ItemRegistry.get_item_class(data['item']['_type']).from_dict(data['item']),
            is_origin=data['is_origin'],
            is_locked=data['is_locked']
        )