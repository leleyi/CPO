from lab1.src.HashMap import *

class HashTableMutable(HashMap):
    MIN_SIZE = 8

    def __init__(self):
        super().__init__(self.MIN_SIZE)

    def put(self, key, value):
        rv = super().put(key, value)
        # increase size of dict * 2 if filled >= 2/3 size (like python dict)
        if len(self) >= (self.size * 2) / 3:
            self.__resize()

    def __resize(self):
        self.size *= 2  # this will be the new size
        self._len = 0
        self.kvEntry = [self._empty] * self.size
        for entry in self.kvEntry:
            if entry is not self._empty and entry is not self._deleted:
                self.put(key, value)
