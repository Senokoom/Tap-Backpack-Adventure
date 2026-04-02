from classes.Inventory.Inventory import Inventory


class ActiveInventory(Inventory):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.owner = None

    def add_item(self, item, x, y):
        super().add_item(item, x, y)
        self.owner.update_stats()

    def remove_item(self, item):
        super().remove_item(item)
        self.owner.update_stats()

    def move_item(self, item, x, y):
        super().move_item(item, x, y)

    def get_rotated_idiot(self, item):
        super().get_rotated_idiot(item)