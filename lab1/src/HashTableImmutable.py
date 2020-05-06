from lab1.src.HashMap import *


class HashTableImmutable(HashMap):
    def __init__(self,  hashmap=None, size=11, **kwds):
        self.size = size
        self._len = 0
        self.kvEntry = [self._empty] * size
        self.index = 0
        if kwds.__len__() != 0:
            hashmap = HashMap(**kwds)
        if hashmap is not None:
            for entry in hashmap.kvEntry:
                if entry is hashmap._empty or entry is hashmap._deleted:
                    continue
                else:
                    print("do this?")
                    super(HashTableImmutable, self).put(entry.key, entry.value)

    def put(self, key, value):
        print("It's a immutable version put.It will return a new HashTableImmutable.")

        table = HashMap()
        table.put(key, value)
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                table.put(entry.key, entry.value)

        return HashTableImmutable(table)

    def put_dic(self, **kwargs):
        print("It's a immutable version put_dic.It will return a new HashTableImmutable.")
        table = HashMap()
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                table.put(entry.key, entry.value)
        table.put_dic(**kwargs)

        return HashTableImmutable(table)

    def del_(self, key):
        print("It's a immutable version.It will return a new HashTableImmutable.")
        table = HashMap()
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                table.put(entry.key, entry.value)
        table.del_(key)

        return HashTableImmutable(table)
