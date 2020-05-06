import unittest
from hypothesis import given
import hypothesis.strategies as st
# from lab1.src.HashTable import *
from lab1.src.HashMap import *


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_size(self):
        table = HashMap()
        for i in range(0, 8):
            table.put(i, i)
        print(table.__len__())
        self.assertEqual(table.__len__(), 11)

    def test_put(self):
        table = HashMap()
        table.put(1, 2)
        print(table.get(5))
        # self.assertEqual();

    def test_something(self):
        dic = {'3': 123, '2': 333}
        table = HashMap(**dic)
        # table.put_dic(**dic)
        print(table[3])

    def test_mconcat(self):
        dic = {'1': 123, '2': 333}
        dic2 = {'3': 23, '4': 323}
        table1 = HashMap(**dic)
        table2 = HashMap(**dic2)

        table1.mconcat(table2)
        print(table1.to_list())
        print(table1[3])

    def test_map(self):
        dic2 = {'3': 23, '4': 323}
        table1 = HashMap(**dic2)
        print(table1[3])
        print(table1.to_list())
        self.assertEqual(table1.to_list(), [])

    def test_reduce(self):

    # sum of empty list
        map = HashMap()
        self.assertEqual(map.reduce(lambda st, e: st + e, 0), 0)

        dic2 = {'3': 23, '4': 323}
        table1 = HashMap(**dic2)
    # sum of map
        self.assertEqual(table1.reduce(lambda st, e: st + e, 0), 346)


if __name__ == '__main__':
    unittest.main()
