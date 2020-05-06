from HashMap import *
import copy


class HashTableImmutable(HashMap):
    def __init__(self,  hashmap=None, size=11, **kwds):
        self.size = size
        self._len = 0
        self.kvEntry = [self._empty] * size
        self.index = 0

        if hashmap is not None:
            for entry in hashmap.kvEntry:
                if entry is hashmap._empty or entry is hashmap._deleted:
                    continue
                else:
                    super(HashTableImmutable, self).put(entry.key, entry.value)
        elif kwds.__len__() != 0:
            print(kwds)
            super(HashTableImmutable, self).__init__(**kwds)

    def put(self, key, value):
        print("It's a immutable version put.It will return a new HashTableImmutable.")

        table = HashMap()
        for entry in self.kvEntry:
            if entry is self._empty or entry is self._deleted:
                continue
            else:
                table.put(entry.key, entry.value)
        table.put(key, value)

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
