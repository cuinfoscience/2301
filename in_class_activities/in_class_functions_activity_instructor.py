import unittest
import random

def addOne(x):
    '''
    The input x is a real number (can be expressed as fraction)

    Return number plus one
    '''
    return x + 1

def f(x):
    '''
    Map every number of the set A to the number -19 where
    A = {0, 1, 2, 3}. If the input is not in A you should 
    throw an AssertionError
    '''
    assert x in {0, 1, 2, 3}

    return -19

def multiplicative_inverse(x):
    '''
    Return the multiplicative inverse of a number

    Args:
        x (float): any float

    Returns:
        bool: The multiplicative inverse. If you multiply a number
        by its multiplicative inverse you get back the number 1

    bonus: how to handle zero? 
    https://en.wikipedia.org/wiki/Multiplicative_inverse
    '''
    return 1/x

class TestFunction(unittest.TestCase):

    def test_addOne(self):
        self.assertEqual(addOne(5), 6)

    def test_multiplicative_inverse(self):
        from random import choice 
        for j in range(5):
            x = random.choice(range(-100, 100))
            inverse = multiplicative_inverse(x)
            self.assertEqual(x * inverse, 1)

    def test_f_no_error(self):
        # the syntax for this method is a little unclear.
        # assertRaises takes three arguments here
        #   1. the exception you expect
        #   2. the function, in this case f
        #   3. the input
        self.assertEqual(f(2), -19)

    def test_f_error(self):
        # the syntax for this method is a little unclear.
        # assertRaises takes three arguments here
        #   1. the exception you expect
        #   2. the function, in this case f
        #   3. the input
        self.assertRaises(AssertionError, f, 10)

if __name__ == '__main__':
    unittest.main()