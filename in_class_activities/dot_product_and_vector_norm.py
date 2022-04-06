import unittest
import math


def dot_product(x, y):
    '''
    Return the dot product of two vectors

    Args:
        x (list): a vector
        y (list): a vector, with same dimensionality as x

    Returns:
        vector: x \\cdot y
    '''
    return 9


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
    return math.sqrt(sum[i ** 2 for i in x])


def normalize_vector(x):
    '''
    Return \\hat{\boldsymbol{x}}, the normalized form of x

    hint: you will need to use euclidean_norm
    '''
    return []


class TestFunction(unittest.TestCase):

    def test_dot_product1(self):
        y = [1, 0]
        x = [0, 1]
        prod = dot_product(x, y)
        self.assertEqual(prod, 0)

    def test_dot_product2(self):
        y = [1, 2, 0]
        x = [0, 1, 1]
        prod = dot_product(x, y)
        self.assertEqual(prod, 2)

    def test_vector_norm(self):
        x = [-2, 2, 1]
        xhat = normalize_vector(x)
        self.assertEqual(euclidean_norm(xhat), 1)


if __name__ == '__main__':
    unittest.main()
