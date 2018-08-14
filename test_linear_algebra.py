import unittest
from linear_algebra import *

class Linear_algebra_test(unittest.TestCase):
    def test_vector_add(self):
        va = vector_add([1, 2, 3], [2, 4, 6])
        self.assertEqual(va, [3, 6, 9])

if __name__ == '__main__':
    unittest.main()
