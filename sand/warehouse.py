class Warehouse:
    def __init__(self):
        self.__map = {}

    def set(self, key, value):
        self.__map[key] = value
        print('set', self.__map)

    def unset(self, key):
        del self.__map[key]

    def read(self, key):
        print('read', self.__map)
        return self.__map[key]
