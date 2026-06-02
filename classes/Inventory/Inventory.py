from cell import Cell

#так же тупо для дебага, потом убрать
# class Item:
#     def __init__(self, name, width, height):
#         self.name = name
#         self.width = width
#         self.height = height





class Inventory:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        x = width * height//3
        self.inventory_matrix = [[Cell() for _ in range(width)] for _ in range(height)]
        for cell in self.inventory_matrix[0]:
            cell.is_locked = False
        self.item_list = []

#Функционал инвенторя
#-----------------------------------------------------------------------------------
    def add_item(self, item, x, y):
        """
        Короч, эта хуйня добавляет пытается добавить предмет по координатам
        x - длина
        y - высота !!!!
        """
        if self.can_fit(item, x, y):
            self.unchecked_add_item(item, x, y)


    def unchecked_add_item(self, item, x, y):
        self.item_list.append(item)
        self.inventory_matrix[x][y].item = item
        for i in range(x, x + item.width):
            for j in range(y, y + item.height):
                self.inventory_matrix[i][j].item = item
                self.inventory_matrix[i][j].is_origin = False
        self.inventory_matrix[x][y].is_origin = True
        item.origin_x = x
        item.origin_y = y

    def remove_item(self, item):
        x = item.origin_x
        y = item.origin_y
        for j in range(x, x + item.width):
            for i in range(y, y + item.height):
                self.inventory_matrix[i][j].item = None
                self.inventory_matrix[i][j].is_origin = False
        self.inventory_matrix[x][y].is_origin = False
        self.item_list.remove(item)
        item.origin_x = None
        item.origin_y = None

#отсылочка :)
    def get_rotated_idiot(self, item):
        x = item.origin_x
        y = item.origin_y
        item.width, item.height = item.height, item.width
        if self.can_fit(item, item.origin_x, item.origin_y):
            self.remove_item(item)
            self.unchecked_add_item(item, x, y)
        else:
            item.width, item.height = item.height, item.width
        return


    def move_item(self, item, x, y):
        if self.can_fit(item, x, y):
            self.remove_item(item)
            self.unchecked_add_item(item, x, y)
        else:
            return

    def can_fit(self, item, x, y):
        if x + item.width > self.width or y + item.height > self.height:
            return False
        for i in range(x, x + item.width):
            for j in range(y, y + item.height):
                if self.inventory_matrix[i][j].is_locked:
                    return False
                if self.inventory_matrix[i][j].item is not None:
                    if self.inventory_matrix[i][j].item == item:
                        pass
                    else:
                        return False
        return True

    def unlock_cell(self, x, y):
        if not self.inventory_matrix[x][y].is_locked:
            return False
        else:
            self.inventory_matrix[x][y].is_locked = False
        return True

    #debag BS
#-------------------------------------------------------------------------
    def item_list_to_string(self):
        item_list_string = ""
        for item in self.item_list:
            item_list_string += item.name + "\n"
        return item_list_string

    def inventory_to_string(self):
        inventory_string = ""
        cell: Cell
        for row in self.inventory_matrix:
            for cell in row:
                inventory_string += cell.to_string()
            inventory_string += "\n"
        return inventory_string


deb_inventory = Inventory(7, 7)
print(deb_inventory.inventory_to_string())
deb_item = Item("debug", 1, 2)
deb_inventory.add_item(deb_item, 0, 0)
print(deb_inventory.item_list_to_string())
print(deb_inventory.inventory_to_string())