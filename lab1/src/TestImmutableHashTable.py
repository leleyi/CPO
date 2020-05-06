import unittest
from lab1.src.HashTableImmutable import *

class MyTestCase(unittest.TestCase):

    def test_put(self):
        table = HashTableImmutable()
        n = table.put(5, 111)
        print(table)
        print(n)
        # self.assertEqual(table.put(5, 111).get(5), 111)

    def test_get(self):
        dic = {'3': 23, '4': 323}
        table = HashTableImmutable(**dic)
        print(table.get(3))


if __name__ == '__main__':
    unittest.main()
