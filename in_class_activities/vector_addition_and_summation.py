import unittest
import math


def vector_addition(x, y):
    '''
    Return the sum of two vectors

    Args:
        x (list): a vector
        y (list     ): a vector, with same dimensionality as x

    Returns:
        vector: x + y
    '''
    out = []
    return out


def euclidean_norm(x):
    '''
    Return the square root of the sum of squares in x
    This is one common way to define the length of a vector

    i.e. $ \\sqrt{ \\sigma x_i^2}$

    Args:
        x (list): a vector

    Returns:
        float: the root of the sum of squares in x
    '''
    out = 0
    return out


class TestFunction(unittest.TestCase):

    def test_vector_addition(self):
        y = [-1, 1]
        x = [9, 1]
        sum_ = vector_addition(x, y)
        self.assertEqual(sum_[0], 8)

    def test_vector_addition2(self):
        y = [-1, 1]
        x = [9, 1]
        sum_ = vector_addition(x, y)
        self.assertEqual(len(sum_), 2)

    def test_vector_addition3(self):
        y = [-1, 1, 9, 10]
        x = [9, 1, 10, 11]
        sum_ = vector_addition(x, y)
        self.assertEqual(sum_[3], 21)

    def test_euclidean_norm(self):
        x = [-1, 1]
        self.assertEqual(euclidean_norm(x), math.sqrt(2))

    def test_euclidean_norm2(self):
        z = [-1, 1, 3]
        self.assertEqual(euclidean_norm(z), math.sqrt(11))


if __name__ == '__main__':
    unittest.main()
