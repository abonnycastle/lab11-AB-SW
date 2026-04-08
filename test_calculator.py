import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(4,5),9)
        self.assertEqual(add(1,1),2)
        self.assertEqual(add(2,5),7)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,0),3)
        self.assertEqual(subtract(10,5),5)
        self.assertEqual(subtract(12,2),10)
    ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3,5),15)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(6,1),6)
    ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        self.assertRaises(divide(5,0),ZeroDivisionError())

    def test_logarithm(self): # 3 assertions
        self.assertEquals(logarithm(2,8),3)
        self.assertEquals(logarithm(10,1),0)
        self.assertEquals(logarithm(5,25),2)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(logarithm(0,10), ValueError())
    ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        self.assertRaises(logarithm(6,0), ValueError())


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(6, 8), 10)


    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        self.assertRaises(square_root(-1), ValueError())


# Do not touch this
if __name__ == "__main__":
    unittest.main()