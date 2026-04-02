from classes.Inventory.Inventory import Inventory


class BackpackInventory(Inventory):
    def __init__(self, width, height):
        super().__init__(width, height)

    def add_item(self, item, x, y):
        super().add_item(item, x, y)

    def remove_item(self, item):
        super().remove_item(item)

    def move_item(self, item, x, y):
        super().move_item(item, x, y)

    def get_rotated_idiot(self, item):
        super().get_rotated_idiot(item)