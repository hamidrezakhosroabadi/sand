from kazoo.client import KazooClient
from constants import DEFAULT_PATH


class Coordinator():

    def __init__(self, zookeeper_host, hostname):
        self.__zookeeper_host = zookeeper_host
        self.__hostname = hostname
        self.__connection = KazooClient(hosts=self.__zookeeper_host)

    def start(self):
        self.__connection.start()
        self.__connection.create(DEFAULT_PATH, self.__hostname, ephemeral=True)

    def stop(self):
        self.__connection.stop()

    def exists(self, hostname):
        return self.__connection.exists(DEFAULT_PATH+hostname)

    def get_members(self):
        return self.__connection.get_children(DEFAULT_PATH)

    def __repr__(self):
        return f'{type(self.__name__)}({self.__zookeeper_host!r},{self.last_name!r})'
