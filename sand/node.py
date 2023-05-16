from requests import get, post, delete


class Node:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def is_lock(self, key):
        return True if get(f'{self.__address}/lock/{key}').status_code == 200 else False

    def lock(self, key):
        post(f'{self.__address}/lock/{key}')

    def unlock(self, key):
        delete(f'{self.__address}/lock/{key}')
