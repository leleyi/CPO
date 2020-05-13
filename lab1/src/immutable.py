from mutable import *


def cons(map):
    table = HashMap()
    table.from_dict(map.to_dict())
    return table


def size(map):
    if map is None:
        return 0
    else:
        return len(map)

"""the order is not change"""

def to_dict(map):
    kvlist = {}
    if map is None:
        return kvlist
    for entry in map.kvEntry:
        if entry is map._empty or entry is map._deleted:
            continue
        else:
            kvlist[entry.key] = entry.value
    return kvlist


def to_list(map):
    res = []
    if map is None:
        return res
    for key in map._keyset:
        res.append(map.get(key))
    return res


def put(map, key, value):
    table = cons(map)
    table.put(key, value)
    return table


def get(map, key):
    return map.get(key)


def put_dic(map, **kwargs):
    table = cons(map)
    table.put_dic(**kwargs)
    return table


def del_(map, key):
    table = cons(map)
    table.del_(key)
    return table


def mconcat(map1, map2):
    if map1 is None:
        return map2
    if map2 is None:
        return map1
    tabel = cons(map1)
    tabel.mconcat(map2)
    return tabel


def map(map, f):
    table = cons(map)
    for key in map._keyset:
        value = map.get(key)
        value = f(value)
        table.put(key, value)
    return table


def reduce(map, f, initial_state):
    state = initial_state
    for key in map._keyset:
        value = map.get(key)
        state = f(state, value)
    return state
