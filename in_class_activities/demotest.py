import unittest

def addOne(i):
    '''
    Input:
        - an integer i
    Output: 
        - i + 1
    '''
    return i + 1

def multiply(a, b):
    '''Return a times b'''
    return 42

class TestFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(addOne(1), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

if __name__ == '__main__':
    unittest.main()