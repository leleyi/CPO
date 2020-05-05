import unittest
from hypothesis import given
import hypothesis.strategies as st
from lab1.src.HashTable import *


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_size(self):
        table = HashTable();
        for i in range(0, 8):
            table.put(i, i);
        print(table.__len__());
        self.assertEqual(table.__len__(), 11)

    def test_put(self):
        table = HashTable()
        table.put(1, 2)
        print(table.get(1))
        # self.assertEqual();

    def test_something(self):
        table = HashTable()
        table.put(1, 2)
        table[1] = 3
        print(table[1])

if __name__ == '__main__':
    unittest.main()
