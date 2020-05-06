from HashTable import *


class HashTableImmutable(HashTable):
    def put(self, key, value):
        print("It's a immutable version.It will return a new HashTableImmutable.")
        dic = {key: value}
        return HashTableImmutable(**dic)

    def put_dic(self, **kwargs):
        print("It's a immutable version.It will return a new HashTableImmutable.")
        return HashTableImmutable(**kwargs)


