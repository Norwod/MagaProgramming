class Warrior:
    def __init__(self, name = "Warrior", health = 100, damage = 20):
        self.name = name
        self.health = health
        self.damage = damage

    def sortByHealth(self):
        return self.health
