import unittest
from lab1.src.HashTableImmutable import *

class MyTestCase(unittest.TestCase):

    def test_put(self):
        table = HashTableImmutable()
        temp = table.put(5, 111)
        print(table)
        print(temp)
        self.assertEqual(temp.get(5), 111)

    def test_get(self):
        dic = {'3': 23, '4': 323}
        table = HashTableImmutable(**dic)
        self.assertEqual(table.get(3), 23)

    def test_del_(self):
        dic = {'3': 23, '4': 323}
        table = HashTableImmutable(**dic)
        temp = table.del_(3)
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
        dic3 = {'1': 123, '2': 333,'3': 23, '4': 323}
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
