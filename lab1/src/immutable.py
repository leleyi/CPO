from mutable import *
from typing import TypeVar, Generator
from typing import List, Dict

V = TypeVar('V', str, int, float, None)
T2 = TypeVar('T2', str, int, float)

def cons(map: HashMap) -> HashMap:
    """
    Copy a hash map

    :param map: HashMap
    :return: The copied hash map
    """
    table = HashMap()
    table.from_dict(map.to_dict())
    return table


def size(map: HashMap) -> int:
    """
    Get the size of the hash map

    :param map: HashMap
    :return: the size of the hash map
    """
    if map is None:
        return 0
    else:
        return len(map)


def to_dict(map: HashMap) -> Dict:
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


def to_list(map: HashMap) -> List:
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

def from_list(list: List) -> HashMap:
    """
    Convert list to hash map

    :param list: list
    :return: The converted hash map
    """
    table = HashMap()
    for i, v in enumerate(list):
        table.put(i, v)
    return table


def put(map: HashMap, key: int, value: V) -> HashMap:
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


def get(map: HashMap, key: int):
    """
    Get the corresponding content from the hash map according to the specified key value

    :param map: HashMap
    :param key: key
    :return: value
    """
    return map.get(key)


def del_(map: HashMap, key: int) -> HashMap:
    """
    Delete the value of the given key from the hash map

    :param map: HashMap
    :param key: key
    :return: HashMap
    """
    table = cons(map)
    table.del_(key)
    return table


def mconcat(map1: HashMap, map2: HashMap) -> HashMap:
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

    table1 = cons(map1)
    table2 = cons(map2)

    if table2 is not None:
        for key in table2._keyset:
            if (table1.get(key) != None):
                value1 = table1.get(key)
                value2 = table2.get(key)
                if (value1 < value2):
                    table1.put(key, value1)
                else:
                    table1.put(key, value2)
            else:
                value = table2.get(key)
                table1.put(key, value)
    return table1


def map(map: HashMap, f: Generator[str, int, float]) -> HashMap:
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


def reduce(map: HashMap, f: Generator[str, int, float], initial_state: T2):
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


def get_hash(map: HashMap, key: int) -> int:
    """
    get the hash_value that had saved the map

    :param map: HashMap
    :param key:
    :return: hash_value
    """
    return map.get_hash(key)


def __eq__(a, b):
    return a.__dict__ == b.__dict__
