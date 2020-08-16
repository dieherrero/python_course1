import random as rnd
from .magic import Spell
import pprint


# COLORES: SE ABRE CON bcolors.color y es OBLIGATORIO CERRAR con bcolors.ENDC
class bcolors:
    HEADER = '\033[095m'
    OKBLUE = '\033[094m'
    OKGREEN = '\033[093m'
    OKRED = '\033[091m'
    ENDC = '\033[0m'  # cierra


import random as rnd


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic attack", "Items"]

    def gen_damage(self):
        return rnd.randrange(self.atkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp >= self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + self.name)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_spell(self):
        i = 1

        for spell in self.magic:
            print(str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("ITEMS:")
        for item in self.items:
            print(str(i) + ".", item["item"].name, ":", item["item"].description, "(x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):  # BARRAS DE VIDA Y MANA
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4  # 25 ticks

        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10  # 10 ticks

        # Aseguramos que la longitud de las barras sea siempre la misma
        while bar_ticks > 0:
            hp_bar += "?"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "+"
            mp_bar_ticks -= 1

        while len(mp_bar) < mp_bar_ticks:
            mp_bar += " "

        # Ajustamos las barras para que marquen bien la vida e incluya espacios en blanco
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decr = 9 - len(hp_string)

            while decr > 0:
                current_hp += " "
                decr -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decr = 7 - len(mp_string)
            while decr > 0:
                current_mp += " "
                decr -= 1

            current_mp = mp_string
        else:
            current_mp = mp_string

        print(self.name + ":", current_hp + " |" + bcolors.OKBLUE + hp_bar + bcolors.ENDC + "|"
              , "   ", current_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2  # 50 ticks
        # Aseguramos que la longitud de las barras sea siempre la misma
        while bar_ticks > 0:
            hp_bar += "€"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        # Ajustamos las barras para que marquen bien la vida e incluya espacios en blanco
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decr = 9 - len(hp_string)

            while decr > 0:
                current_hp += " "
                decr -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print(self.name + ":", current_hp + " |" + bcolors.OKBLUE + hp_bar + bcolors.ENDC + "|")
