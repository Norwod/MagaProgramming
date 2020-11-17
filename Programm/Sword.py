from Programm.Weapon import Weapon
import random


class Sword(Weapon):

    def __init__(self, damage, durability = 100):
        self.damage = damage
        self.durability = durability

    def attack(self):
        attack_damage = self.damage * (self.durability * 0.01)
        if random.randint(0, 1) == 0:
            self.durability -= 10
        return attack_damage
        


