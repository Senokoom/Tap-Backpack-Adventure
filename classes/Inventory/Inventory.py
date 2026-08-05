from numpy.core.multiarray import item

from classes.Inventory.cell import Cell


class Inventory:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # x = width * height//3
        self.inventory_matrix = [[Cell() for _ in range(width)] for _ in range(height)]
        for row in self.inventory_matrix:
            for cell in row:
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
            return True
        else:
            return False


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
        for i in range(x, x + item.width):
            for j in range(y, y + item.height):
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
            item.width, item.height = item.height, item.width
            self.remove_item(item)
            item.width, item.height = item.height, item.width
            self.unchecked_add_item(item, x, y)
            return True
        else:
            item.width, item.height = item.height, item.width
            return False


    def move_item(self, item, x, y):
        if self.can_fit(item, x, y):
            self.remove_item(item)
            self.unchecked_add_item(item, x, y)
            return True
        else:
            return False

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

    def unlock_cell(self, y, x):
        if not self.inventory_matrix[y][x].is_locked:
            return False
        else:
            self.inventory_matrix[y][x].is_locked = False
        return True

### СОЗДАНИЕ DICT ДЛЯ СОХРАНЕНИЯ В JSON И ОБРАТНО.
    @classmethod
    def from_dict(cls, data):
       inventory = cls(
            width=data['width'],
            height=data['height']
        )
       for cell in data["matrix"]:
           i = cell['i']
           j = cell['j']
           restored_cell = Cell.from_dict(cell['cell_info'])
           if 0 <= i < inventory.height and 0 <= j < inventory.width:
               inventory.inventory_matrix[i][j] = restored_cell
               if restored_cell.item and restored_cell.is_origin:
                   inventory.item_list.append(restored_cell.item)
       return inventory

    def to_dict(self):
        result_dict = {
            "width": self.width,
            "height": self.height,
            "matrix": [],
            "items": []
        }
        for i in range(self.height):
            for j in range(self.width):
                result_dict["matrix"].append(
                    {
                        "i": i,
                        "j": j,
                        "cell_info": self.inventory_matrix[i][j].to_dict()
                    }
                )
        for item in self.item_list:
            result_dict["items"].append(item.to_dict())
        return result_dict


    def __lt__(self, other):
        return len(self.item_list) < len(other.item_list)

    def __eq__(self, other):
        return len(self.item_list) == len(other.item_list)

    def __str__(self):
        return f"{self.inventory_to_string()}"


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

#так же тупо для дебага, потом убрать
class Item:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height


# ДЕБАЖИЛ
# deb_inventory = Inventory(7, 7)
# print(deb_inventory.inventory_to_string())
# deb_item = Item("debug", 3, 1)
# deb_inventory.add_item(deb_item, 0, 0)
#
# print(deb_inventory.inventory_to_string())
#
# deb_inventory.get_rotated_idiot(deb_item)
#
# print(deb_inventory.inventory_to_string())