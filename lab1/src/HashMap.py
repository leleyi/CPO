class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str("{" + str(self.key) + ": " + str(self.value) + "}")


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

    def __init__(self, size=11, **kwds):
        self.size = size
        self._len = 0
        self.kvEntry = [self._empty] * size
        self.index = 0

        print(kwds)
        """init_by_dict"""
        if kwds.__len__() != 0:
            print("feiji")
            self.put_dic(**kwds)

    def put(self, key, value):
        initial_hash = hash_ = self.hash(key)

        while True:
            if self.kvEntry[hash_] is self._empty or self.kvEntry[hash_] is self._deleted:
                # can assign to hash_ index
                self.kvEntry[hash_] = Node(key, value)
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
                self._len -= 1
                return

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def to_dict(self):
        kvlist = {}
        if self.size == 0:
            return kvlist
        else:
            for entry in self.kvEntry:
                if entry is self._empty or entry is self._deleted:
                    continue
                else:
                    kvlist[str(entry.key)] = entry.value
        return kvlist
    """
        get the hash value
    """

    def hash(self, key):
        return key % self.size

    """
        open address  (linear probing)
    """

    def _rehash(self, old_hash):
        return (old_hash + 1) % self.size

    """put value dict"""

    def put_dic(self, **kwargs):
        for k, v in kwargs.items():
            self.put(int(k), v)

    def mempty(self):
        self.kvEntry = [self._empty] * self.size()

    def mconcat(self, other):
        if self.size == 0:
            return other
        for entry in other.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                self.put(entry.key, entry.value)

    def map(self, f):
        for entry in self.kvEntry:
            if entry is self._empty:
                continue
            else:
                value = f(entry.value)
                self.put(entry.key, value)

    def reduce(self, f, initial_state):
        state = initial_state
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                value = entry.value
                state = f(state, value)
        return state

    def __iter__(self):
        return self.kvEntry

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration("end")
        else:
            self.index += 1
            return self.kvEntry[self.index - 1]

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
                res = res + str(entry.key)+":"+str(entry.value) + ","
        return "{" + res[0:-1] + "}"



# class ResizableHashTable(HashMap):
#     MIN_SIZE = 8
#
#     def __init__(self):
#         super().__init__(self.MIN_SIZE)
#
#     def put(self, key, value):
#         rv = super().put(key, value)
#         # increase size of dict * 2 if filled >= 2/3 size (like python dict)
#         if len(self) >= (self.size * 2) / 3:
#             self.__resize()
#
#     def __resize(self):
#         keys, values = self._keys, self._values
#         self.size *= 2  # this will be the new size
#         self._len = 0
#         self.kvEntry = [self._empty] * self.size
#         for key, value in zip(keys, values):
#             if key is not self._empty and key is not self._deleted:
#                 self.put(key, value)
