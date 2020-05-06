class HashTable(object):
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

    #
    # def __setattr__(self, key, value):
    #     raise AttributeError('不可变类')

    def __init__(self, size=11, **kwds):
        # super().__setattr__()
        # self.capacity = 0;
        self.size = size
        self._len = 0
        self._keys = [self._empty] * size  # keys
        self._values = [self._empty] * size  # values
        """init_by_dict"""
        if kwds.__len__() != 0:
            self.put_dic(**kwds)

    def put(self, key, value):
        initial_hash = hash_ = self.hash(key)

        while True:
            if self._keys[hash_] is self._empty or self._keys[hash_] is self._deleted:
                # can assign to hash_ index
                self._keys[hash_] = key
                self._values[hash_] = value
                self._len += 1
                return
                # key already exists here, assign over
            elif self._keys[hash_] == key:
                self._keys[hash_] = key
                self._values[hash_] = value
                return

            # the collision get a new hash_value
            hash_ = self._rehash(hash_)

            # if there is no place to put eg initial_hash == hash_
            if initial_hash == hash_:
                raise ValueError("Table is full")

    def get(self, key):
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                # That key was never assigned
                return None
            elif self._keys[hash_] == key:
                # key found
                return self._values[hash_]

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def del_(self, key):
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                # That key was never assigned
                return None
            elif self._keys[hash_] == key:
                # key found, assign with deleted sentinel
                self._keys[hash_] = self._deleted
                self._values[hash_] = self._deleted
                self._len -= 1
                return

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def to_list(self):
        kvlist = [self._empty] * size
        if self._empty:
            return kvlist
        else:
            for i, key in self._keys:
                value = self.get(key)
                kvlist[i] = Node(key, value)
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

    def size(self):
        return self.size

    def map(self):
        return None

    def reduce(self):
        return None

    def __iter__(self):
        return None

    def __next__(self):
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.del_(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self._len


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.key + " : " + self.value)


class ResizableHashTable(HashTable):
    MIN_SIZE = 8

    def __init__(self):
        super().__init__(self.MIN_SIZE)

    def put(self, key, value):
        rv = super().put(key, value)
        # increase size of dict * 2 if filled >= 2/3 size (like python dict)
        if len(self) >= (self.size * 2) / 3:
            self.__resize()

    def __resize(self):
        keys, values = self._keys, self._values
        self.size *= 2  # this will be the new size
        self._len = 0
        self._keys = [self._empty] * self.size
        self._values = [self._empty] * self.size
        for key, value in zip(keys, values):
            if key is not self._empty and key is not self._deleted:
                self.put(key, value)