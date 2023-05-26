from functools import total_ordering
from hashlib import md5
from sys import byteorder


@total_ordering
class object:
    def __init__(self, key):
        self.__key = key

    def __hash__(self):
        return int.from_bytes(md5(f'{self.__key}'.encode()).digest(), byteorder)

    def __lt__(self, obj):
        return hash(self) < hash(obj)

    def __eq__(self, obj):
        return hash(self) == hash(obj)

    def __repr__(self):
        return f'{type(self).__name__}({self.__key!r})'
