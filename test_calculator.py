#https://github.com/kgreen5-art/lab11
#Partner 1: Kaesi Green
# Partner 2: Kai West
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,4), 6)
        self.assertEqual(add(-3, 8), 5)
        self.assertEqual(add(-6, -7), -13)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(4,2), 2)
        self.assertEqual(sub(2, 8), -6)
        self.assertEqual(sub(-4, 7), -11)
        self.assertEqual(sub(-6, -7), 1)

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,2),2)
        self.assertEqual(mul(-1, 2), -2)
        self.assertEqual(mul(-100, -2), 200)
    #     fill in code

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(20, 2), 10)
        self.assertEqual(div(20, -2), -10)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(3, 0)
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(3, 27), 3)
        self.assertEqual(logarithm(5, 625), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-3, 9)
        with self.assertRaises(ValueError):
            logarithm(0, 9)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-10, -10)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    import math
    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(-4,-9), math.hypot(-4,-9))
        self.assertEqual(hypotenuse(1,4), math.hypot(1, 4))
        self.assertEqual(hypotenuse(-182,929), math.hypot(-182,929))
    #     fill in code

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1000)
        with self.assertRaises(ValueError):
            square_root(-100)
        self.assertEqual(2, square_root(4))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
