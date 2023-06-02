import unittest
from unittest.mock import patch
import pytest
from app.calc import Calculator,InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    #Sumar
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(1, self.calc.add(0, 1))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    #Restar
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))
        self.assertEqual(-1, self.calc.substract(0, 1))
    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    #Multiplicar
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(1, -2))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(0, self.calc.multiply(0,-1))

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    #Dividir
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(2.5, self.calc.divide(5, 2))
        self.assertEqual(-1, self.calc.divide(2, -2))
        self.assertEqual(1.5, self.calc.divide(-3, -2))
        self.assertEqual(-2.5, self.calc.divide(-5, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)
        self.assertRaises(TypeError, self.calc.divide, None, 0)

    #Potencia
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(4, self.calc.power(-2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(0, 0))
        self.assertEqual(0, self.calc.power(0, 3))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
    #Raiz cuadrada
    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.square_root(16))
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(0, self.calc.square_root(0))
        self.assertEqual(5, self.calc.square_root(25))

    def test_square_root_method_returns_correct_result_negative_values(self):
        self.assertEqual("4.0 * i", self.calc.square_root(-16))
        self.assertEqual("2.0 * i", self.calc.square_root(-4))
        self.assertEqual(0, self.calc.square_root(-0))
        self.assertEqual("5.0 * i", self.calc.square_root(-25))

    def test_square_root_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square_root, "2")
        self.assertRaises(TypeError, self.calc.square_root, "-2")
        self.assertRaises(TypeError, self.calc.square_root, None)
        self.assertRaises(TypeError, self.calc.square_root, object())
        self.assertRaises(TypeError, self.calc.square_root, 100, 5)

    #Logaritmo
    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.logarithm(10))
        self.assertEqual(0, self.calc.logarithm(1))
        self.assertEqual(2, self.calc.logarithm(100))
        self.assertEqual(4, self.calc.logarithm(10000))
    
    def test_logarithm_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.logarithm, -10)
        self.assertRaises(TypeError, self.calc.logarithm, -1)
        self.assertRaises(TypeError, self.calc.logarithm, -100)
        self.assertRaises(TypeError, self.calc.logarithm, -10000)

    def test_logarithm_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.logarithm, "2")
        self.assertRaises(TypeError, self.calc.logarithm, None)
        self.assertRaises(TypeError, self.calc.logarithm, object())
        self.assertRaises(TypeError, self.calc.logarithm, 100, 5)
    
    #Chequear valores
    def test_check_types_method_returns_correct_result(self):
        self.assertEqual(None, self.calc.check_types(10,21))
        self.assertEqual(None, self.calc.check_types(-8,5))
        self.assertEqual(None, self.calc.check_types(8,-5))
        self.assertEqual(None, self.calc.check_types(2.5,0))
        self.assertEqual(None, self.calc.check_types(0,2.5))

    def test_check_types_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_types, 100, None)
        self.assertRaises(TypeError, self.calc.check_types, None, 1)
        self.assertRaises(TypeError, self.calc.check_types, 100, object())
        self.assertRaises(TypeError, self.calc.check_types, object(), 1)
        self.assertRaises(TypeError, self.calc.check_types, "2", 1)
        self.assertRaises(TypeError, self.calc.check_types, 100, "2")

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
