from functools import total_ordering
from hashlib import md5
from sys import byteorder


class Value:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def get_key(self):
        return str(self.__key)

    def get_value(self):
        return self.__value

    def __hash__(self):
        return int.from_bytes(md5(f'{self.__key}'.encode()).digest(), byteorder)

    def __lt__(self, obj):
        return hash(self) < hash(obj)

    def __eq__(self, obj):
        return hash(self) == hash(obj)

    def __repr__(self):
        return f'{type(self).__name__}({self.__key!r},{self.__value!r})'
