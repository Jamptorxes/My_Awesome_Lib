import unittest
from my_awesome_lib.math_tools import *


class TestMathTools(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 2), 1)

    def test_silnia(self):
        self.assertEqual(silnia(0), 1)
        self.assertEqual(silnia(1), 1)
        self.assertEqual(silnia(2), 2)
        self.assertEqual(silnia(3), 6)
        self.assertEqual(silnia(4), 24)
        self.assertEqual(silnia(5), 120)
        with self.assertRaises(ValueError):
            silnia(-1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_pierwsza(self):
        self.assertTrue(pierwsza(2))
        self.assertTrue(pierwsza(3))
        self.assertFalse(pierwsza(26))
        self.assertFalse(pierwsza(27))


if __name__ == "__main__":
    unittest.main()
