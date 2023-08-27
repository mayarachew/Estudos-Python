from unittest import TestCase
from calculator import Calculator

class TestCalculator(TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(4,6),10)
        self.assertEqual(Calculator.add(5,5),10)
        self.assertEqual(Calculator.add(4,-1),3)
        self.assertEqual(Calculator.add(-1,4),3)
        self.assertEqual(Calculator.add(-7,6),-1)
        self.assertEqual(Calculator.add(7,-6),1)
        self.assertEqual(Calculator.add(-7,7),0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(4,6),-2)
        self.assertEqual(Calculator.subtract(5,5),0)
        self.assertEqual(Calculator.subtract(4,-1),5)
        self.assertEqual(Calculator.subtract(-1,4),-5)
        self.assertEqual(Calculator.subtract(-7,6),-13)
        self.assertEqual(Calculator.subtract(7,-6),13)
        self.assertEqual(Calculator.subtract(-7,7),-14)

    def test_divide(self):
        self.assertEqual(Calculator.divide(4,5),0.8)
        self.assertEqual(Calculator.divide(5,5),1)
        self.assertEqual(Calculator.divide(4,-1),-4)
        self.assertEqual(Calculator.divide(-1,4),-0.25)
        self.assertEqual(Calculator.divide(-7,4),-1.75)
        self.assertEqual(Calculator.divide(7,-4),-1.75)
        self.assertEqual(Calculator.divide(-7,-7),1)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4,5),20)
        self.assertEqual(Calculator.multiply(5,5),25)
        self.assertEqual(Calculator.multiply(4,-1),-4)
        self.assertEqual(Calculator.multiply(-1,4),-4)
        self.assertEqual(Calculator.multiply(-7,4),-28)
        self.assertEqual(Calculator.multiply(7,-4),-28)
        self.assertEqual(Calculator.multiply(-7,-7),49)

        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)
