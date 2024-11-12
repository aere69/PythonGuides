import unittest
import main

class TestIntegerCalculatorMethods(unittest.TestCase):
    def setup(self):
        pass

    def test_addition(self):
        self.assertEqual(main.add(4,3),7)

    def test_substraction(self):
        self.assertEqual(main.substract(4,3),1)

    def test_multiplication(self):
        self.assertEqual(main.multiply(5,3),15)

    def test_division(self):
        self.assertEqual(main.divide(15,3),5)

if __name__ == '__main__':
    unittest.main(verbosity=2)