import unittest

from mutable import *
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
        table.put(2, 5)  # update the value to 5;
        self.assertEqual(table.get(2), 5)
        table.put(3, 5)  # allow have the same value;
        self.assertEqual(table.get(3), 5)

    def test_del(self):
        table = HashMap()
        dict = {1: 2, 2: 3, 3: 4}
        table.from_dict(dict)
        del table[1]
        dict2 = {2: 3, 3: 4}
        self.assertEqual(table.to_dict(), dict2)

    def test_mempty(self):
        table = HashMap()
        dict = {1: 2, 2: 3, 3: 4}
        table.from_dict(dict)
        table.mempty()
        self.assertEqual(table.to_dict(), {})

    def test_size(self):
        table = HashMap()
        self.assertEqual(len(table), 0)
        table.put(1, 2)
        self.assertEqual(len(table), 1)
        table.put(2, 3)
        self.assertEqual(len(table), 2)

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
        table.from_dict(dict1)
        tmp = {}
        for e in table:
            tmp[e.key] = e.value
        self.assertEqual(table.to_dict(), tmp)
        i = iter(HashMap())
        self.assertRaises(StopIteration, lambda: next(i))

    def test_hash_collision(self):
        table1 = HashMap()
        table2 = HashMap()
        table1.put(1, 3)
        table2.put(12, 3)
        self.assertEqual(table1.get_hash(1), table2.get_hash(12))
        # means the key of 1 and 12 have the same hash_value;
        # put the the key that have same init_hash_value
        table1.put(12, 4)

        # now they have different hash_value, beacase the collision happen, to deal the collision the key rehash unit have not coollision
        self.assertNotEqual(table1.get_hash(12), table2.get_hash(12))

    # we fixed the max_size because we delete the Capacity Expansion that we have implemented before
    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        dict = HashMap()
        dict.from_list(a)
        b = dict.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        dict = HashMap()
        dict.from_list(a)
        self.assertEqual(len(dict), len(a))

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()))
    def test_monoid_identity(self, a, b):
        dict_a = HashMap()
        dict_b = HashMap()
        dict_a.from_list(a)
        dict_b.from_list(b)
        a_b = dict_a.mconcat(dict_b)  # {}
        b_a = dict_b.mconcat(dict_a)  # {}
        self.assertEqual(a_b, b_a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        dict_a = HashMap()
        dict_b = HashMap()
        dict_c = HashMap()
        dict_a.from_list(a)  # {}
        dict_b.from_list(b)  # {}
        dict_c.from_list(c)  # {0 0}
        a_b = dict_a.mconcat(dict_b)  # {}
        b_a = dict_b.mconcat(dict_a)  # {}
        self.assertEqual(a_b, b_a)
        c_b = dict_c.mconcat(dict_b)  # {0,0}
        b_c = dict_b.mconcat(dict_c)  # {0,0}
        self.assertEqual(c_b, b_c)
        a_b__c = dict_c.mconcat(a_b)
        a__b_c = dict_a.mconcat(b_c)
        self.assertEqual(a_b__c, a__b_c)

    @given(st.lists(st.integers()))
    def test_from_list2(self, a):
        dict = HashMap()
        dict.from_list(a)
        self.assertEqual(dict.to_list(), a)

    @given(a=st.integers(), b=st.integers())
    def test_put2(self, a, b):
        table = HashMap()
        table.put(a, b)
        self.assertEqual(table.get(a), b)


if __name__ == '__main__':
    unittest.main()
