from Programm.Weapon import Weapon
import random


class Bow(Weapon):

    def __init__(self, damage, chance):
        self.__damage = damage
        self.__chance = chance

    def potential_damage(self):
        return self.__damage * (self.__chance * 0.01)

    def attack(self):
        chance_attack = self.__chance * 0.01
        rn = random.random()
        if rn <= chance_attack:
            return self.__damage
        else:
            return 0

