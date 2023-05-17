from sortedcontainers import SortedSet
from node import Node


class Ring:
    def __init__(self, nodes):
        self.__nodes = SortedSet(nodes)

    def add(self, node):
        self.__nodes.add(node)

    def remove(self, node):
        self.__nodes.remove(node)

    def get(self, obj, replicas):
        bisect_index = self.__nodes.bisect(obj)
        return [self.__nodes[bisect_index+i] for i in range(replicas)]

    def __len__(self):
        return len(self.__nodes)

    def __repr__(self):
        return f'{type(self).__name__}({list(self.__nodes)!r})'
