import unittest
from hypothesis import given
import hypothesis.strategies as st
# from lab1.src.HashTable import *
from lab1.src.HashMap import *
from lab1.src.HashTableMutable import *

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_put(self):
        table = HashTableMutable()
        table.put(1, 3)
        self.assertEqual(table.get(1), 3)

    def test_size(self):
        self.assertEqual(table.__len__(), 0)
        table.put(1, 2)
        self.assertEqual(table.__len__(), 1)
        table.put(2, 3)
        self.assertEqual(table.__len__(), 2)

    def test_todict(self):
        table = HashMap()
        table.put(4, 5)
        test_data = {'1': 2, '2': 3, '3': 4}
        table.put_dic(**test_data)
        test_data = {'1': 2, '2': 3, '3': 4, '4': 5}
        self.assertEqual(table.to_dict(), test_data)

        # self.assertEqual();

    def test_from_dict(self):
        test_data = {'1': 2, '2': 3, '3': 4}
        table = HashMap(**test_data)
        self.assertEqual(table.to_dict(),test_data)


    def test_mconcat(self):
        dic = {'1': 123, '2': 333}
        dic2 = {'3': 23, '4': 323}
        dic3 = {'1': 123, '2': 333,'3': 23, '4': 323}
        table1 = HashMap(**dic)
        table2 = HashMap(**dic2)
        table1.mconcat(table2)
        self.assertEqual(table1.to_dict(), dic3)

    def test_map(self):
        dic2 = {'3': 23, '4': 323}
        dic3 = {'3': '23', '4': '323'}
        table1 = HashMap(**dic2)
        table1.map(str)
        self.assertEqual(table1.to_dict(), dic3)

    def test_reduce(self):
        map = HashMap()
        self.assertEqual(map.reduce(lambda st, e: st + e, 0), 0)
        dic2 = {'3': 23, '4': 323}
        table1 = HashMap(**dic2)
        self.assertEqual(table1.reduce(lambda st, e: st + e, 0), 346)


if __name__ == '__main__':
    unittest.main()
