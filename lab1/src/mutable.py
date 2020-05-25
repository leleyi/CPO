from typing import TypeVar
from typing import List


class Node:
    def __init__(self, key, value):
        """
        init the map node
        :param key: key value
        :param value: value
        """
        self.key = key
        self.value = value

    def __repr__(self):
        return str("{" + str(self.key) + ":" + str(self.value) + "}")

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


V = TypeVar(str, int, float)


class HashMap(object):
    """
    HashMap Data Type
    HashMap() Create a new, empty map. It returns an empty map collection.
    put(key, val) Add a new key-value pair to the map. If the key is already in the map then replace
                    the old value with the new value.
    get(key) Given a key, return the value stored in the map or None otherwise.
    del_(key) or del map[key] Delete the key-value pair from the map using a statement of the form del map[key].
    len() Return the number of key-value pairs stored in the map.
    in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
    """

    _empty = object()
    _deleted = object()

    def __init__(self, dict=None):
        """

        :param dict: init_the map by a dict if dict is not null
        """
        self.size = 11
        self._len = 0
        self.kvEntry = [self._empty] * self.size
        self._keyset = [] * self.size
        self.index = 0
        """init_by_dict"""
        if dict is not None:
            self.from_dict(dict)

    def put(self, key: int, value: V):
        """

        :param key: map key_value
        :param value:map value
        :return:
        """
        if self._len > self.size - 2:
            self.capacity_extension()

        initial_hash = hash_ = self.hash(key)

        while True:
            if self.kvEntry[hash_] is self._empty or self.kvEntry[hash_] is self._deleted:
                # can assign to hash_ index
                self.kvEntry[hash_] = Node(key, value)
                self._keyset.append(key)
                self._len += 1
                return
                # key already exists here, assign over
            elif self.kvEntry[hash_].key == key:
                self.kvEntry[hash_] = Node(key, value)
                return
            # the collision get a new hash_value
            hash_ = self._rehash(hash_)

            # if there is no place to put eg initial_hash == hash_
            if initial_hash == hash_:
                raise ValueError("Table is full")

    def put_entry(self, entry: Node):
        """
        put a k_v entry
        :param entry: a k_v node
        """
        key = entry.key, value = entry.value
        self.put(key, value)
        return self

    def get(self, key: int) -> V:
        """
        get the storage value in map where key = key
        :param key: key
        :return: map value
        """
        initial_hash = hash_ = self.hash(key)
        while True:
            if self.kvEntry[hash_] is self._empty or self.kvEntry[hash_] is self._deleted:
                # That key was never assigned
                return None
            elif self.kvEntry[hash_].key == key:
                # key found
                return self.kvEntry[hash_].value

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def del_(self, key: int) -> V:
        """
        delete the map node in map where the key = key
        :param key: map value
        :return:  map value
        """
        initial_hash = hash_ = self.hash(key)
        while True:
            if self.kvEntry[hash_] is self._empty or self.kvEntry[hash_] is self._deleted:
                # That key was never assigned
                return None
            elif self.kvEntry[hash_].key == key:
                # key found, assign with deleted sentinel
                self.kvEntry[hash_] = self._deleted
                self._keyset.remove(key)
                self._len -= 1
                return

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    """the order is not change"""
    """from dict"""

    def from_dict(self, dict):
        """
        insert the data from the python dictionary type
        :param dict: {key, value}
        """
        for k, v in dict.items():
            self.put(int(k), v)

    def to_dict(self):
        """
        convert this map to the dict {}
        :return: {key, value}
        """
        kvlist = {}
        for item in self.items():
            kvlist[item.key] = item.value
        return kvlist

    def from_list(self, list: List):

        """
        add the map value from list make the i,v(enumerate) to the k and v
        :param list: list like [1,2,31,5]
        """
        if list:
            for i, v in enumerate(list):
                self.put(i, v)

        return self

    def to_list(self) -> List:
        """
        make this map to a list. just use the values in the map
        :return: []
        """
        res = []
        for key in self._keyset:
            res.append(self.get(key))
        return res

    """
        get the hash value
    """

    def items(self) -> List:
        """
        get all the items in the map
        :return: items []
        """
        items = []
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                items.append(entry)
        return items

    def hash(self, key: int) -> int:
        """
        get the hash value by the method
        :param key: key
        :return: hash_value
        """
        return key % self.size

    def get_hash(self, key: int) -> int:

        initial_hash = hash_ = self.hash(key)
        while True:
            if self.kvEntry[hash_] is self._empty or self.kvEntry[hash_] is self._deleted:
                # That key was never assigned
                return hash_
            elif self.kvEntry[hash_].key == key:
                # key found
                return hash_
            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    """
        open address  (linear probing)
    """

    def _rehash(self, old_hash: int) -> int:
        """
        if the hash collision happened should invoke this method
        :param old_hash: the hash_value collision
        :return: new hash_value
        """
        return (old_hash + 1) % self.size

    def capacity_extension(self):
        """
        if the capacity is not enough extension the capacity
        size = size * 2
        """
        self.kvEntry.extend([self._empty] * self.size)
        self._keyset.extend([] * self.size)
        self.size = 2 * self.size
        return self

    def mempty(self):
        """
        clear the map
        """
        self.kvEntry = [self._empty] * self.size
        return self

    def mconcat(self, other):
        """
        concat two maps to one
        :param other:  map
        :return: map
        """
        if self is None:
            return other

        if other is not None:
            for key in other._keyset:
                value = other.get(key)
                self.put(key, value)

        return self

    def map(self, f):
        """
        map the map element to the f
        :param f: the function to map
        """
        for key in self._keyset:
            value = self.get(key)
            value = f(value)
            self.put(key, value)
        return self

    def reduce(self, f, initial_state):
        """
        reduce the mapSet to one value
        :param f: the reduce method
        :param initial_state:result initial_state
        :return:final res
        """
        state = initial_state
        for key in self._keyset:
            value = self.get(key)
            state = f(state, value)
        return state

    def __iter__(self):
        return iter(self.items())

    def __next__(self):
        if self.index >= self._len:
            raise StopIteration("end")
        else:
            self.index += 1
            val = self.get(self._keyset[self.index - 1])
            return key, val

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.del_(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self._len

    # {'1': 2, '2': 3, '3': 4}
    def __repr__(self):
        res = ""
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                res = res + str(entry.key) + ":" + str(entry.value) + ","
        return "{" + res[0:-1] + "}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ or self.to_dict() == other.to_dict()
