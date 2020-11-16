class Warrior:
    def __init__(self, name = "Warrior", health = 100, damage = 20):
        self.name = name
        self.health = health
        self.damage = damage

    def printInformation(self):
        print('Воин под именем:' + self.name + ' имеет ' + str(self.health) + ' здоровья и имеет ' + str(self.damage) + ' урона.')

    def __del__(self):
        print("Valhalla, " + self.name + " is coming.")