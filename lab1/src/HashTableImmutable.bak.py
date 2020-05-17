from lab1.src.mutable import *


class HashTableImmutable(HashMap):
    def __init__(self,  hashmap=None, size=11, **kwds):
        self.size = size
        self._len = 0
        self.kvEntry = [self._empty] * size
        self.index = 0
        self._keyset = [] * size
        if kwds.__len__() != 0:
            hashmap = HashMap(**kwds)
        if hashmap is not None:
            for key in hashmap._keyset:
                super(HashTableImmutable, self).put(key, hashmap.get(key))

    def put(self, key, value):

        table = HashMap()
        for k in self._keyset:
            table.put(k, self.get(k))
        table.put(key, value)

        return HashTableImmutable(table)

    def put_dic(self, **kwargs):
        table = HashMap()
        for key in self._keyset:
            table.put(key, self.get(key))
        table.put_dic(**kwargs)

        return HashTableImmutable(table)

    def del_(self, key):
        table = HashMap()
        for k in self._keyset:
            table.put(k, self.get(k))
        table.del_(key)
        return HashTableImmutable(table)

    def mconcat(self, other):
        table = HashMap()
        for key in self._keyset:
            table.put(key, self.get(key))

        for key in other._keyset:
            table.put(key, other.get(key))

        return HashTableImmutable(table)

    def map(self, f):
        table = HashMap()
        for key in self._keyset:
            value = self.get(key)
            value = f(value)
            table.put(key, value)
        return table

