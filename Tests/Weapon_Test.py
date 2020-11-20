import unittest
from Programm.Weapon import Weapon


class TestWeaponMethods(unittest.TestCase):
    def test_name(self):
        w = Weapon("Меч")
        self.assertEqual(w.name, "Меч")
        self.assertNotEqual(w.name, "Лук")

    def test_damage_getter(self):
        w = Weapon()
        self.assertEqual(w.damage, 10)
        w1 = Weapon("Воие", 20)
        self.assertEqual(w1.damage, 20)

    def test_damage_setter(self):
        w = Weapon("Меч")
        self.assertEqual(w.damage, 10)
        w.damage = 20.0
        self.assertEqual(w.damage, 20)

    def test_le_1(self):
        w1 = Weapon("Меч 1", 20)
        w2 = Weapon("Меч 2", 10)
        self.assertFalse(w1.__le__(w2))

    def test_le_2(self):
        w1 = Weapon("Меч 1", 20)
        w2 = Weapon("Меч 2", 10)
        self.assertTrue(w2.__le__(w1))

if __name__ == '__main__':
    unittest.main()

