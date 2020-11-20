import unittest
from Programm.Bow import Bow


class TestBowMethods(unittest.TestCase):
    def test_name(self):
        b = Bow()
        self.assertEqual(b.name, "Лук")
        self.assertNotEqual(b.name, "Мкч")
        self.assertEqual(b.damage, 6.0)
        self.assertEqual(b.chance, 60)

    def test_attack(self):
        b = Bow("Лук", 50, 25)
        self.assertEqual(b.damage, 12.5)

    def test_le_1(self):
        b1 = Bow("Лук", 50, 25)
        b2 = Bow("Лук2", 15, 100)
        self.assertTrue(b1.__le__(b2))


    def test_le_2(self):
        b1 = Bow("Лук", 50, 25)
        b2 = Bow("Лук2", 15, 75)
        self.assertFalse(b1.__le__(b2))

if __name__ == '__main__':
    unittest.main()

