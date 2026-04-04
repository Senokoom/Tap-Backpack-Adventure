from classes.Item.Armor import Armor
from classes.Item.Trinket import Trinket
from classes.Item.Weapon import Weapon
from classes.Item.Consumable import Consumable
from DataManagment.DataLoader import get_weapon_data


class ItemGenerator:

    def __init__(self):
        weapon_data = get_weapon_data()
        self.weapon, self.suffix, self.prefix = weapon_data["weapon"], weapon_data["suffix"], weapon_data["prefix"]
        self.rarity_weights = {
            "common": 70,
            "uncommon": 15,
            "rare": 10,
            "epic": 5,
            "legendary": 1
        }


    #Генерирует СТРОГО оружие
    def generate_weapon(self) -> Weapon:
       pass


    def create_weighted_lists(self):
        pass

    def apply_weights_bonus(self, bonus):
       return



