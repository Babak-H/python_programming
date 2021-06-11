# the naming convention is to write test_nameOfModule when making test
# https://docs.python.org/3/library/unittest.html

import unittest
import calc


class TestCase(unittest.TestCase):

    # name of method should start with test_
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(10, -5), 5)
        self.assertEqual(calc.add(5, 0), 5)
        self.assertEqual(calc.add(-1, -3), -4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, -5), -50)
        self.assertEqual(calc.multiply(5, 0), 0)
        self.assertEqual(calc.multiply(1, 3), 3)

    def test_divide(self):
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertEqual(calc.divide(5, 1), 5)
        self.assertEqual(calc.divide(-3, -1), 3)
        self.assertEqual(calc.divide(5, 2), 2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(3, 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, -5), 15)
        self.assertEqual(calc.subtract(5, 0), 5)
        self.assertEqual(calc.subtract(-1, -3), 2)


if __name__ == '__main__':
    unittest.main()





