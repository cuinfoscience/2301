import unittest
import math
from random import random

def flip_coin(p=.5):
    '''
    Return 1 for heads with probability p
    Return 0 for tails, with probability 1-p
    '''
    if random() < p:
        return 1
    else:
        return 0

def two_flips():
    '''
    Perform an experiment where you flip a fair coin two times.

    Return a string of 1s and 0s showing outcome of the 
    experiment. This is sometimes called a bitstring. 
    
    For instance, if you get two heads you should return "11"
    If you get a head and tails you should return "10"
    '''
    return str(flip_coin()) + str(flip_coin())

def find_omega(N=1000):
    '''
    Perform the two_flips experiment N=1000 times 
    and return the set of all possible outcomes (i.e. omega)
    '''
    out = set()
    for i in range(N):
        out.add(two_flips())
    return out

class TestFunction(unittest.TestCase):

    def test_two_flips_len(self):
        flips = two_flips()
        self.assertEqual(len(flips), 2)

    def test_two_flips_type(self):
        flips = two_flips()
        self.assertEqual(type(flips), type("a str"))

    def test_omega_size(self):
        omega = find_omega()
        self.assertEqual(len(omega), 4)

    def test_omega_value(self):
        omega = find_omega()
        self.assertEqual({"00", "01", "11", "10"}, omega)

if __name__ == '__main__':
    unittest.main()