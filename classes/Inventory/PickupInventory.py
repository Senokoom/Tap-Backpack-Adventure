from classes.Inventory.Inventory import Inventory


class PickupInventory(Inventory):
    def __init__(self, width, height):
        super().__init__(width, height)

    def remove_item(self, item):
        super().remove_item(item)

    def move_item(self, item, x, y):
        super().move_item(item, x, y)

    def get_rotated_idiot(self, item):
        super().get_rotated_idiot(item)