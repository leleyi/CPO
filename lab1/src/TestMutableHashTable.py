import unittest

from lab1.src.HashMap import *


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_put(self):
        table = HashMap()
        table.put(2, 3)
        self.assertEqual(table.get(2), 3)

    def test_del(self):
        table = HashMap()
        test_data = {1: 2, 2: 3, 3: 4}
        table.put_dic(test_data)
        del table[1]
        test_data = {2: 3, 3: 4}
        self.assertEqual(table.to_dict(), test_data)

    def test_mempty(self):
        table = HashMap()
        test_data = {1: 2, 2: 3, 3: 4}
        table.put_dic(test_data)
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
        test_data = {1: 2, 2: 3, 3: 4}
        table.put_dic(test_data)
        test_data = {1: 2, 2: 3, 3: 4, 4: 5}
        self.assertEqual(table.to_dict(), test_data)

    def test_from_dict(self):
        test_data = {1: 2, 2: 3, 3: 4}
        table = HashMap(test_data)
        self.assertEqual(table.to_dict(), test_data)

    def test_to_list(self):
        test_data = {1: 2, 2: 3, 3: 4}
        table = HashMap(test_data)
        self.assertEqual(table.to_list(), [2, 3, 4])

    def test_mconcat(self):
        dic = {1: 123, 2: 333}
        dic2 = {3: 23, 4: 323}
        dic3 = {1: 123, 2: 333, 3: 23, 4: 323}
        table1 = HashMap(dic)
        table2 = HashMap(dic2)
        table1.mconcat(table2)
        self.assertEqual(table1.to_dict(), dic3)

    def test_map(self):
        dic2 = {3: 23, 4: 323}
        dic3 = {3: '23', 4: '323'}
        table1 = HashMap(dic2)
        table1.map(str)
        self.assertEqual(table1.to_dict(), dic3)

    def test_reduce(self):
        map = HashMap()
        self.assertEqual(map.reduce(lambda st, e: st + e, 0), 0)
        dic2 = {3: 23, 4: 323}
        table1 = HashMap(dic2)
        self.assertEqual(table1.reduce(lambda st, e: st + e, 0), 346)

    def test_iter(self):
        dic3 = {1: 123, 2: 333, 3: 23, 4: 323}
        table = HashMap()
        table.put_dic(dic3)
        tmp = {}
        for e in table:
            tmp[e.key] = e.value
        self.assertEqual(table.to_dict(), tmp)
        i = iter(HashMap())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()
