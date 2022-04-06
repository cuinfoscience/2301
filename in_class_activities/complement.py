import unittest


def complement(A, U):
    '''Return the complement of A, assuming A is in a universe U
    '''
    return 42

class TestFunction(unittest.TestCase):

    def test_complement(self):
        self.assertEqual(type(complement({2}, {1,2})), set)

    def test_complement2(self):
        A = {1, 2}
        U = {1, 2, 3, 4}
        self.assertEqual(complement(A, U), {3, 4})

if __name__ == '__main__':
    unittest.main()