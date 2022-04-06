import unittest
from random import random


def flip_coin(p):
    '''
    Return 1 for heads and 0 for tails,
    with probability p
    '''
    if random() < p:
        return 1
    else:
        return 0


def compute_mean(flips):
    '''
    Input is a list of binary digits

    Return the mean of the list, which is
    also equal to the fraction of 1s in the list
    '''
    return 0


class TestFunction(unittest.TestCase):

    def test_mean(self):
        flips = [0, 1]
        mean = compute_mean(flips)
        self.assertEqual(mean, 0.5)


if __name__ == '__main__':
    unittest.main()
