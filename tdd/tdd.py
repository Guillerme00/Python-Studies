import unittest
from math_operations import add_operation, sub_operation, mult_operation, divide_operation

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        math_add_result = add_operation(n1 = 5, n2 = 10)
        self.assertEqual(math_add_result, 15)

    def test_sub(self):
        math_sub_result = sub_operation(n1 = 5, n2 = 10)
        self.assertEqual(math_sub_result, -5)

    def test_mult(self):
        math_mult_result = mult_operation(n1 = 5, n2 = 10)
        self.assertEqual(math_mult_result, 50)

    def test_divide(self):
        math_divide_result = divide_operation(n1 = 10, n2 = 5)
        self.assertEqual(math_divide_result, 2)


if __name__ == "__main__":
    unittest.main()