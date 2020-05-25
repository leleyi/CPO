import unittest
from lab1.src.immutable import *
from hypothesis import given
import hypothesis.strategies as st


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
        self.assertEqual(to_dict(del_(put(HashMap(), 1, 2), 1)), {})

    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(put(HashMap(), 1, 2)), [2])
        self.assertEqual(to_list(put(put(HashMap(), 1, 2), 2, 3)), [2, 3])

    def test_from_list(self):
        lis = [1, 2]
        self.assertEqual(to_list(from_list([])), [])
        self.assertEqual(to_list(from_list(lis)), lis)

    def test_mconcat(self):
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(to_dict(mconcat(put(HashMap(), 1, 2), None)), to_dict(put(HashMap(), 1, 2)))
        self.assertEqual(to_dict(mconcat(None, put(HashMap(), 1, 2))), to_dict(put(HashMap(), 1, 2)))

    def test_map(self):
        self.assertEqual(to_dict(map(HashMap(), str)), {})
        self.assertEqual(to_dict(map(put(HashMap(), 1, 2), str)), {1: '2'})

    def test_reduce(self):
        self.assertEqual(reduce(HashMap(), lambda st, e: st + e, 0), 0)
        self.assertEqual(reduce(HashMap({'3': 23, '4': 323}), lambda st, e: st + e, 0), 346)

    def test_iter(self):
        table = HashMap({1: 123, 2: 333, 3: 23, 4: 323})
        tmp = {}
        for e in table:
            tmp[e.key] = e.value
        self.assertEqual(to_dict(table), tmp)
        i = iter(HashMap())
        self.assertRaises(StopIteration, lambda: next(i))

    def test_immutability(self):
        table1 = HashMap()
        table2 = put(table1, 1, 2)
        self.assertNotEqual(id(table1), id(table2))
        table3 = del_(table2, 1)
        self.assertNotEqual(id(table2), id(table3))
        table4 = mconcat(table2, table3)
        self.assertNotEqual(id(table4), id(table2))
        self.assertNotEqual(id(table4), id(table3))
        table5 = map(table4, str)
        self.assertNotEqual(id(table4), id(table5))

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), key=st.integers(), value=st.integers())
    def test_immutable(self, a, b, key, value):
        table = from_list(a)
        table1 = put(table, key, value)
        self.assertNotEqual(id(table), id(table1))
        table3 = del_(table, key)
        self.assertNotEqual(id(table1), id(table3))
        table4 = from_list(b)
        table5 = mconcat(table3, table4)
        table6 = mconcat(table4, table3)
        self.assertNotEqual(id(table5), id(table6))

    def test_hash_collision(self):
        table1 = HashMap()
        table2 = HashMap()
        table1 = put(table1, 1, 3)
        table2 = put(table2, 12, 3)
        self.assertEqual(get_hash(table1, 1), get_hash(table2, 12))
        # means the key of 1 and 12 have the same hash_value;
        # put the the key that have same init_hash_value
        table1 = put(table1, 12, 4)

        # now they have different hash_value, beacase the collision happen, to deal the collision the key rehash unit have not coollision
        self.assertNotEqual(get_hash(table1, 12), get_hash(table2, 12))

    @given(st.lists(st.integers()))  # the map
    def test_from_list_to_list_equality(self, a):
        dict = from_list(a)
        b = to_list(dict)
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        dict = from_list(a)
        self.assertEqual(len(dict), len(a))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        self.assertEqual(mconcat(None, a), a)
        self.assertEqual(mconcat(a, None), a)

    @given(st.lists(st.integers()))
    def test_from_list(self, lst):
        a = from_list(lst)
        self.assertEqual(to_list(a), lst)

    @given(st.lists(st.integers()))
    def test_to_list(self, lst):
        a = from_list(lst)
        self.assertEqual(to_list(a), lst)

    @given(key=st.integers(), value=st.integers())
    def test_put(self, key, value):
        dict = put(HashMap(), key, value)
        self.assertEqual(get(dict, key), value)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        dict_a = from_list(a)  # {}
        dict_b = from_list(b)  # {0:0}
        dict_c = from_list(c)  # {0:1}
        a_b = mconcat(dict_a, dict_b)  # {0:0}
        b_a = mconcat(dict_b, dict_a)  # {0:0}
        self.assertEqual(to_dict(a_b), to_dict(b_a))
        c_b = mconcat(dict_c, dict_b)  # {0:0}
        b_c = mconcat(dict_b, dict_c)  # {0:0}
        self.assertEqual(to_dict(c_b), to_dict(b_c))
        a_b__c = mconcat(dict_c, a_b)
        a__b_c = mconcat(dict_a, b_c)
        self.assertEqual(to_dict(a_b__c), to_dict(a__b_c))
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(mconcat(None, dict_a), dict_a)
        self.assertEqual(mconcat(dict_a, None), dict_a)
        print(a_b__c,a__b_c)


if __name__ == '__main__':
    unittest.main()
