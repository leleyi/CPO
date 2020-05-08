from lab1.src.HashMap import *


def cons(map):
    table = HashMap();
    for k in map._keyset:
        table.put(k, map.get(k))
    return table

def put(map, key, value):
    table = cons(map)
    table.put(key, value)
    return table


def put_dic(map , **kwargs):
    table = cons(map)
    table.put_dic(**kwargs)
    return table


def del_(map, key):
    table = cons(map)
    table.del_(key)
    return table


def mconcat(map1, map2):
    tabel = cons(map)
    tabel.mconcat(map2)
    return tabel


def map(self, f):
    table = HashMap()
    for key in self._keyset:
        value = self.get(key)
        value = f(value)
        table.put(key, value)
    return table
