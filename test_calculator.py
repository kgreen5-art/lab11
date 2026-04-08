#https://github.com/kgreen5-art/lab11
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(1,2),2)
        self.assertEqual(multiply(-1, 2), -2)
        self.assertEqual(multiply(-100, -2), 200)
    #     fill in code

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(2, 20), 10)
        self.assertEqual(divide(-2, 20), -10)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        if logarithm(1, -1):
            self.assertRaises(ValueError, logarithm(9, -10))
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
        self.assertRaises(ValueError, square_root(-1000))
        self.assertRaises(ValueError, square_root(-100))
        self.assertEqual(2, square_root(4))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()