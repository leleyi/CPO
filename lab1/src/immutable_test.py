import unittest
from lab1.src.immutable import *


class MyTestCase(unittest.TestCase):

    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(HashMap()), 0)
        self.assertEqual(size(put(HashMap(), 1, 2)), 1)

    def test_put(self):
        self.assertEqual(to_dict(put(HashMap(), 1, 2)), {1: 2})
        self.assertEqual(to_dict(put(put(HashMap(), 1, 2), 2, 3)), {1: 2, 2: 3})

    def test_get(self):
        self.assertEqual(get(put(HashMap(), 1, 2), 1), 2)
        self.assertEqual(get(put(HashMap(), 3, 4), 3), 4)

    def test_del_(self):
        self.assertEqual(to_dict(put(HashMap(), 1, 2)), {1: 2})

        self.assertEqual(table.get(3), 23)
        self.assertEqual(temp.get(3), None)

    def test_to_dict(self):
        dic = {'3': 23, '4': 323}
        table = HashTableImmutable(**dic)
        temp = table.to_dict()
        self.assertEqual(temp, dic)

    def test_mconcat(self):
        dic = {'1': 123, '2': 333}
        dic2 = {'3': 23, '4': 323}
        dic3 = {'1': 123, '2': 333, '3': 23, '4': 323}
        table1 = HashTableImmutable(**dic)
        table2 = HashTableImmutable(**dic2)
        temp = table1.mconcat(table2)
        self.assertEqual(temp.to_dict(), dic3)
        self.assertEqual(table1.to_dict(), dic)
        self.assertEqual(table2.to_dict(), dic2)

    def test_map(self):
        dic2 = {'3': 23, '4': 323}
        dic3 = {'3': '23', '4': '323'}
        table1 = HashTableImmutable(**dic2)
        temp = table1.map(str)
        self.assertEqual(table1.to_dict(), dic2)
        self.assertEqual(temp.to_dict(), dic3)

    def test_reduce(self):
        table1 = HashTableImmutable()
        self.assertEqual(table1.reduce(lambda st, e: st + e, 0), 0)
        dic2 = {'3': 23, '4': 323}
        table2 = HashTableImmutable(**dic2)
        self.assertEqual(table2.reduce(lambda st, e: st + e, 0), 346)


if __name__ == '__main__':
    unittest.main()
