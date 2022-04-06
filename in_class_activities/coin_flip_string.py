import unittest
from random import random


def num_heads(coinString):
    '''
    returns the number of heads in the string

    input is of the form TT, HHH, THTHT etc.
    '''
    count = 0
    return count


class TestFunction(unittest.TestCase):

    def test_num_heads(self):
        num = num_heads("HHT")
        self.assertEqual(num, 2)


if __name__ == '__main__':
    unittest.main()
