import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator(2, 1)
        r = calc.add()
        self.assertEqual(3, r)

    def test_sub(self):
        calc = Calculator(2, 1)
        r = calc.sub()
        self.assertEqual(1, r)

    def test_mul(self):
        calc = Calculator(2, 1)
        r = calc.mul()
        self.assertEqual(2, r)

    def test_div(self):
        calc = Calculator(2, 1)
        r = calc.div()
        self.assertEqual(2, r)

    def test_mod(self):
        calc = Calculator(2, 1)
        r = calc.mod()
        self.assertEqual(0, r)

    def test_pow(self):
        calc = Calculator(2, 3)
        r = calc.pow()
        self.assertEqual(8, r)

    def test_rshift(self):
        calc = Calculator(2, 1)
        r = calc.rshift()
        self.assertEqual(4, r)

    def test_lshift(self):
        calc = Calculator(2, 1)
        r = calc.lshift()
        self.assertEqual(1, r)

    def test_zerodiv(self):
        with self.assertRaises(ZeroDivisionError):
            calc = Calculator(2, 0)
            calc.div()

    def test_difftype(self):
        with self.assertRaises(TypeError):
            calc = Calculator(2, 'l')
            calc.add()