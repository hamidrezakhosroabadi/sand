from requests import get, post, delete


class HTTPClient:
    def read(self, address, key):
        return get(f'{address}/keys/{key}').text

    def set(self, address, key, value):
        post(f'{address}/keys/{key}', json={'value': value})

    def unset(self, address, key):
        delete(f'{address}/keys/{key}')
