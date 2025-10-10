# Unit_Test/test_calculator.py
import unittest
import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 5), 15)

    def test_divide(self):
        self.assertAlmostEqual(Calculator.divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
