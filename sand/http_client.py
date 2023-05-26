from requests import get, post, delete


class HTTPClient:
    def is_lock(self, address, key):
        return True if get(f'{address}{key}').status_code == 200 else False

    def lock(self, address, key):
        post(f'{address}{key}')

    def unlock(self, address, key):
        delete(f'{address}{key}')
