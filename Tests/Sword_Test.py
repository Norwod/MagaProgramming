import unittest
from Programm.Sword import Sword


class TestSwordMethods(unittest.TestCase):
    def test_name(self):
        s = Sword()
        self.assertEqual(s.name, "Меч")
        self.assertNotEqual(s.name, "Лук")
        self.assertEqual(s.damage, 10)

    def test_attack(self):
        s = Sword()
        self.assertEqual(s.damage, 10)
        s.attack()
        self.assertNotEqual(s.damage, 10)
        s.attack()
        self.assertEqual(s.damage, 8)

    def test_damage_setter(self):
        s = Sword()("Меч")
        self.assertEqual(s.damage, 10)
        s.damage = 20.0
        self.assertEqual(s.damage, 20)

    def test_le_1(self):
        s1 = Sword("Меч 1", 20)
        s2 = Sword("Меч 2", 15)
        self.assertFalse(s1.__le__(s2))
        for i in range(1, 50):
            s1.attack()
        self.assertTrue(s1.__le__(s2))


    def test_le_2(self):
        s1 = Sword("Меч 1", 10)
        s2 = Sword("Меч 2", 20)
        self.assertTrue(s1.__le__(s2))
        for i in range(1, 50):
            s2.attack()
        self.assertFalse(s1.__le__(s2))

if __name__ == '__main__':
    unittest.main()

