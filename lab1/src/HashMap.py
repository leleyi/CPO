class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str("{" + str(self.key) + ":" + str(self.value) + "}")

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


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

    def __init__(self, size=11, dict=None):
        self.size = size
        self._len = 0
        self.kvEntry = [self._empty] * size
        self._keyset = [] * size
        self.index = 0

        """init_by_dict"""
        if dict is not None:
            self.put_dic(dict)

    def put(self, key, value):
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

    def put_entry(self, entry):
        key = entry.key, value = entry.value
        self.put(key, value)

    def get(self, key):
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

    def del_(self, key):
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

    def to_dict(self):
        kvlist = {}
        for item in self.items():
            kvlist[item.key] = item.value
        return kvlist

    def to_list(self):
        res = []
        for key in self._keyset:
            res.append(self.get(key))
        return res

    """
        get the hash value
    """

    def items(self):
        items = []
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                items.append(entry)
        return items

    def hash(self, key):
        return key % self.size

    """
        open address  (linear probing)
    """

    def _rehash(self, old_hash):
        return (old_hash + 1) % self.size

    """put value dict"""

    def put_dic(self, dict):
        for k, v in dict.items():
            self.put(int(k), v)

    def mempty(self):
        self.kvEntry = [self._empty] * self.size

    def mconcat(self, other):
        for key in other._keyset:
            value = other.get(key)
            self.put(key, value)

    def map(self, f):
        for key in self._keyset:
            value = self.get(key)
            value = f(value)
            self.put(key, value)

    def reduce(self, f, initial_state):
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
