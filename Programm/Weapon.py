class Weapon:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        if damage in range(1, 100):
            self.__damage = damage
        else:
            print("Недопустимый урон оружия")
