import unittest
from mycalc import Calculator
import dotenv

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(15,3) #Assertion

    def test_add(self):
        x = self.calculator.add()
        self.assertEqual(x,18)

    def test_sub(self):
        x1 = self.calculator.sub()
        self.assertEqual(x1,12)

    # @unittest.SkipTest

    def test_mult(self):
        x2 = self.calculator.mult()
        self.assertEqual(x2,45)

    def test_div(self):
        x3 = self.calculator.div()
        self.assertEqual(x3,5)

if __name__ == '__main__':
    unittest.main()
