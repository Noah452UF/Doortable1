# https://github.com/Noah452UF/Doortable1
# Partner 1 Vivek Jayakumar
# Partner 2 Noah Poston

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
        assert multiply(3, 4) == 12
        assert multiply(10, 10) == 100
        assert multiply(5, 12) == 60


    def test_divide(self): # 3 assertions
        assert divide(10, 10) == 1
        assert divide(5, 25) == 5
        assert divide(3, 39) == 13
    # ##########################

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
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(3, 4) == 5
        assert hypotenuse(2, 2) == square_root(8)
        assert hypotenuse(30, 30 ) == square_root(1800)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        assert square_root(25) == 5
        assert square_root(100) == 10
        with self.assertRaises(ValueError):
            square_root(-1)
#     #    square_root(NUM)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()