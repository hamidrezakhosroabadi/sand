from requests import get, post, delete
from hashlib import md5
from functools import total_ordering
from sys import byteorder


@total_ordering
class Node:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def __hash__(self):
        return int.from_bytes(md5(f'{self.__name}{self.__address}'.encode()).digest(), byteorder)

    def __lt__(self, obj):
        return hash(self) < hash(obj)

    def __eq__(self, obj):
        return hash(self) == hash(obj)

    def __repr__(self):
        return f'{type(self).__name__}({self.__name!r},{self.__address!r})'
