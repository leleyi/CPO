from mutable import *


def cons(map):
    """
    Copy a hash map

    :param map: HashMap
    :return: The copied hash map
    """
    table = HashMap()
    table.from_dict(map.to_dict())
    return table


def size(map):
    """
    Get the size of the hash map

    :param map: HashMap
    :return: the size of the hash map
    """
    if map is None:
        return 0
    else:
        return len(map)


def to_dict(map):
    """
    Convert hash map to dictionary

    :param map: HashMap
    :return: dict
    """
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
    """
    Convert hash map to list

    :param map: HashMap
    :return: list
    """
    res = []
    if map is None:
        return res
    for key in map._keyset:
        res.append(map.get(key))
    return res


# def from_list(map, list):
#     table = cons(map)
#     for i, v in enumerate(list):
#         table.put(i, v)
#     return table

def from_list(list):
    """
    Convert list to hash map

    :param list: list
    :return: The converted hash map
    """
    table = HashMap()
    for i, v in enumerate(list):
        table.put(i, v)
    return table


def put(map, key, value):
    """
    Insert key-value pairs into hash map

    :param map: HashMap
    :param key: The key value to insert into the hash map
    :param value: The content corresponding to the key value of the hash map to be inserted
    :return: Hash map obtained after inserting key-value pairs
    """
    table = cons(map)
    table.put(key, value)
    return table


def get(map, key):
    """
    Get the corresponding content from the hash map according to the specified key value

    :param map: HashMap
    :param key: key
    :return: value
    """
    return map.get(key)


def put_dic(map, **kwargs):
    """
    Convert dict to hash map

    :param map: HashMap
    :param kwargs: A string of key-value pairs
    :return: HashMap
    """
    table = cons(map)
    table.put_dic(**kwargs)
    return table


def del_(map, key):
    """
    Delete the value of the given key from the hash map

    :param map: HashMap
    :param key: key
    :return: HashMap
    """
    table = cons(map)
    table.del_(key)
    return table


def mconcat(map1, map2):
    """
    concat two maps to one

    :param map1: HashMap
    :param map2: HashMap
    :return: HashMap
    """
    if map1 is None and map2 is None:
        return None
    if map1 is None:
        return cons(map2)
    if map2 is None:
        return cons(map1)
    tabel = cons(map1)
    tabel.mconcat(map2)
    return tabel


def map(map, f):
    """
    map the map element to the f

    :param map1: HashMap
    :param f: the function to map
    :return: HashMap
    """
    table = cons(map)
    for key in map._keyset:
        value = map.get(key)
        value = f(value)
        table.put(key, value)
    return table


def reduce(map, f, initial_state):
    """
    reduce the mapSet to one value

    :param map: HashMap
    :param f: the reduce method
    :param initial_state: result initial_state
    :return: final result
    """
    state = initial_state
    for key in map._keyset:
        value = map.get(key)
        state = f(state, value)
    return state


def get_hash(map, key):
    """
    get the hash_value that had saved the map

    :param map: HashMap
    :param key:
    :return: hash_value
    """
    return map.get_hash(key)


def __eq__(a, b):
    return a.__dict__ == b.__dict__
