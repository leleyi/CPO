import unittest
from hypothesis import given
import hypothesis.strategies as st
# from mutable import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
