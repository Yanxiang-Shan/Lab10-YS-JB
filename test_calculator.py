#https://github.com/Yanxiang-Shan/Lab10-YS-JB.git
#Partner 1: Yanxiang Shan
#Partner 2: Jiya Bhatt

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10 ,4), 6)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -10)
        with self.assertRaises(ValueError):
            logarithm(2, 1)

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 2), 6)
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(3, 3), 9)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(6, 2), 3)
        self.assertEqual(div(6, 4), 1.5)
        self.assertEqual(div(6, 3), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-5, 2)
        with self.assertRaises(ValueError):
            logarithm(5, -2)
        with self.assertRaises(ValueError):
            logarithm(5, 1)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertEqual(hypotenuse(12,16),20)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16),4)
# Do not touch this
if __name__ == "__main__":
    unittest.main()