import unittest

from lab1.src.mutable import *


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_put(self):
        table = HashMap()
        table.put(2, 3)
        self.assertEqual(table.get(2), 3)
        self.assertEqual(table.to_dict(), {2: 3})

    def test_del(self):
        table = HashMap()
        dict = {1: 2, 2: 3, 3: 4}
        table.put_dic(dict)
        del table[1]
        dict2 = {2: 3, 3: 4}
        self.assertEqual(table.to_dict(), dict2)

    def test_mempty(self):
        table = HashMap()
        dict = {1: 2, 2: 3, 3: 4}
        table.put_dic(dict)
        table.mempty()
        self.assertEqual(table.to_dict(), {})

    def test_size(self):
        table = HashMap()
        self.assertEqual(table.__len__(), 0)
        table.put(1, 2)
        self.assertEqual(table.__len__(), 1)
        table.put(2, 3)
        self.assertEqual(table.__len__(), 2)

    def test_to_dict(self):
        table = HashMap()
        table.put(4, 5)
        dict1 = {1: 2, 2: 3, 3: 4}
        table.put_dic(dict1)
        dict2 = {1: 2, 2: 3, 3: 4, 4: 5}
        self.assertEqual(table.to_dict(), dict2)

    def test_from_dict(self):
        dict = {1: 2, 2: 3, 3: 4}
        table = HashMap(dict)
        self.assertEqual(table.to_dict(), dict)

    def test_to_list(self):
        dict = {1: 2, 2: 3, 3: 4}
        table = HashMap(dict)
        self.assertEqual(table.to_list(), [2, 3, 4])

    def test_mconcat(self):
        dict1 = {1: 123, 2: 333}
        dict2 = {3: 23, 4: 323}
        dict3 = {1: 123, 2: 333, 3: 23, 4: 323}
        table1 = HashMap(dict1)
        table2 = HashMap(dict2)
        table1.mconcat(table2)
        self.assertEqual(table1.to_dict(), dict3)

    def test_map(self):
        dict1 = {3: 23, 4: 323}
        dict2 = {3: '23', 4: '323'}
        table1 = HashMap(dict2)
        table1.map(str)
        self.assertEqual(table1.to_dict(), dict2)

    def test_reduce(self):
        table = HashMap()
        self.assertEqual(table.reduce(lambda st, e: st + e, 0), 0)
        dict1 = {3: 23, 4: 323}
        table1 = HashMap(dict1)
        self.assertEqual(table1.reduce(lambda st, e: st + e, 0), 346)

    def test_iter(self):
        dict1 = {1: 123, 2: 333, 3: 23, 4: 323}
        table = HashMap()
        table.put_dic(dict1)
        tmp = {}
        for e in table:
            tmp[e.key] = e.value
        self.assertEqual(table.to_dict(), tmp)
        i = iter(HashMap())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()
