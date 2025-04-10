import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10 ,4), 7)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-3, -3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(2, 8), 3.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(-2, 10)
        with self.assertRaises(ValueError):
            log(2, -10)

# Do not touch this
if __name__ == "__main__":
    unittest.main()