import unittest

from mutable import *
from hypothesis import given
import hypothesis.strategies as st
from hypothesis import given
import hypothesis.strategies as st

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

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            dict = HashMap()
            dict.from_list(e)
            self.assertEqual(dict.to_list(), e)

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
        table1 = HashMap(dict1)
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

    def test_hash_collision(self):
        table = HashMap()
        table.put(1, 3)
        table.put(12, 4)
        #the collision happen
        print(table.get_hash(1))
        print(table.get_hash(12))
        print(table.get(1))
        print(table.get(12))
        self.assertEqual(table.get_hash(1), 1)
        self.assertEqual(table.get_hash(12), 2)


    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        dict = HashMap()
        dict.from_list(a)
        b = dict.to_list
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        dict = HashMap()
        dict.from_list(a)
        self.assertEqual(len(dict), len(a))


if __name__ == '__main__':
    unittest.main()
