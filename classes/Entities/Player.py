from numpy import random

from classes.Inventory.ActiveInventory import ActiveInventory
from classes.Inventory.BackpackInventory import BackpackInventory


class Player:

    def __init__(self, id, name, xppoints, gold, level, skill_point, ActiveInventory: ActiveInventory, BackpackInventory: BackpackInventory, last_time_online,
                 active_buffs=None, stats=None):

        self.id = id
        self.name = name
        self.xppoints = xppoints
        self.gold = gold
        self.level = level
        self.skill_point = skill_point
        self.ActiveInventory = ActiveInventory
        self.BackpackInventory = BackpackInventory
        self.last_time_online = last_time_online

        # self.active_buffs = active_buffs
        # if active_buffs is None:
        #     self.active_buffs = []

        self.stats = stats
        if stats is None:
            self.stats = {
                "physical_damage": 1,
                "fire_damage": 1,
                "ice_damage": 1,
                "lightning_damage": 1,
                "emotional_damage": 1,
                "critical_damage": 0.5,
                "critical_damage_chance": 0.01,
                "gold_drop": 1.0,
                "xp_drop": 1.0,
                "item_drop": 0.1,
                "rare_item_chance": 0.05
            }

        self.current_stats = self.stats

    def deal_damage(self):
        #будет высчитывать урон от всех статов, что есть, и отправлять в виде словарика(уже потом будут всякие дебафы идти и т.д.
        physical_damage = self.stats["physical_damage"]
        fire_damage = self.stats["fire_damage"]
        ice_damage = self.stats["ice_damage"]
        lightning_damage = self.stats["lightning_damage"]
        emotional_damage = self.stats["emotional_damage"]
        critical_damage = (physical_damage + fire_damage + ice_damage + lightning_damage + emotional_damage)* (self.stats["critical_damage"] if random.random() <= self.stats["critical_damage_chance"] else 0)
        return{
            "physical_damage": physical_damage,
            "fire_damage": fire_damage,
            "ice_damage": ice_damage,
            "lightning_damage": lightning_damage,
            "emotional_damage": emotional_damage,
            "critical_damage": critical_damage
        }

    def consume_item(self, item):
        potion_info = {"item": item.name, "stats": item.stats, "duration": item.duration}
        self.active_buffs.append(potion_info)
        return


#ДЛЯ СОХРАНЕНИЯ :)
    @classmethod
    def from_dict(cls, data):
        return Player(
            id=data['id'],
            name=data['name'],
            xppoints=data['xppoints'],
            gold=data['gold'],
            level=data['level'],
            skill_point=data['skill_points'],
            ActiveInventory=ActiveInventory.from_dict(data['ActiveInventory']),
            BackpackInventory=BackpackInventory.from_dict(data['BackpackInventory']),
            last_time_online=data['last_time_online'],
            stats=data['stats']
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "xppoints": self.xppoints,
            "gold": self.gold,
            "level": self.level,
            "skill_points": self.skill_point,
            "ActiveInventory": self.ActiveInventory.to_dict(),
            "BackpackInventory": self.BackpackInventory.to_dict(),
            "last_time_online": self.last_time_online,
            "stats": self.stats
        }


    # def active_buffs_update(self, time_passed):
    #     if not self.active_buffs:
    #         return
    #     else:
    #         i = 0
    #         while i < len(self.active_buffs):
    #             self.active_buffs[i]["duration"] -= time_passed
    #             if self.active_buffs[i]["duration"] <= 0:
    #                 self.active_buffs.remove(self.active_buffs[i])
    #             else:
    #                 i += 1

    def skill_levelup(self, skill):
        if self.skill_point > 0:
            self.stats[skill] += 1
            self.skill_point -= 1
        return


