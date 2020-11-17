import math


class Weapon:
    def __init__(self, damage):
        self.__damage = damage

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        if damage in range(0.1, math.inf):
            self.__damage = damage
        else:
            print("Недопустимый урон оружия")
