import random as rnd
class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def gen_damage(self):
        low = self.dmg - 5
        high = self.dmg +5
        return rnd.randrange(low, high)

    def gen_manacost(self):
        return self.cost