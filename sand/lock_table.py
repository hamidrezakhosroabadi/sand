class LockTable:
    def __init__(self):
        self.__table = ['hi']

    def lock(self, key):
        self.__table.append(key)

    def unlock(self, key):
        self.__table.remove(key)

    def is_lock(self, key):
        return key in self.__table
