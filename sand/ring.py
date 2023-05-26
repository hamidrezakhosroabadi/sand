from sortedcontainers import SortedSet
from node import Node
from itertools import cycle


class Ring:
    def __init__(self, nodes):
        self.__nodes = SortedSet(nodes)

    def add(self, node):
        self.__nodes.add(node)

    def remove(self, node):
        self.__nodes.remove(node)

    def get(self, obj, replicas=1):
        if replicas > len(self.__nodes):
            raise Exception()
        bisect_index = self.__nodes.bisect(obj)
        return [self.__nodes[(bisect_index+i) % len(self.__nodes)]
                for i in range(replicas)]

    def get_all(self):
        return list(self.__nodes)

    def __len__(self):
        return len(self.__nodes)

    def __repr__(self):
        return f'{type(self).__name__}({list(self.__nodes)!r})'
