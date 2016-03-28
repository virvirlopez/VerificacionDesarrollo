import unittest
from Calculator import Calculatora


class TestEjemplo(unittest.TestCase):

    def setUp(self):
        pass

    def test_calculator_subtraction(self):
        self.assertEqual(Calculatora.calculate(3, 1, "-"), 2)

    def test_calculator_add(self):
        self.assertEqual(Calculatora.calculate(1, 1, "+"), 2)

    def test_calculator_division(self):
        self.assertEqual(Calculatora.calculate(1, 1, "/"), 1)

    def test_calculator_multiplication(self):
        self.assertEqual(Calculatora.calculate(1, 8, "*"), 8)

    def test_fails_bool(self):
        self.assertRaises(Exception, lambda: Calculatora.calculate(1, True, 1))

    def test_fails_tupla(self):
        self.assertRaises(Exception, lambda: Calculatora.calculate((1, 2, 3), 2, "+"))

    def test_fails_with_one_element(self):
        self.assertRaises(Exception, lambda: Calculatora.calculate(1))

    def test_fails_with_two_element(self):
        self.assertRaises(Exception, lambda: Calculatora.calculate(1, 2))

    def test_fails_number_less_than_0(self):
        self.assertRaises(Exception, lambda: Calculatora.calculate(-1, 1, "+"))
        self.assertRaises(Exception, lambda: Calculatora.calculate(1, -1, "*"))

    def test_fails_number_more_than_100(self):
        self.assertRaises(Exception, lambda: Calculatora.calculate(101, 1, "/"))
        self.assertRaises(Exception, lambda: Calculatora.calculate(101, 1, "-"))


if __name__ == '__main__':
    unittest.main()
