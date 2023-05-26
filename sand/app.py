from warehouse import Warehouse
from node import Node
from os import getenv
from http_client import HTTPClient
from ring import Ring
from flask import Flask, request
from object import object

this_node_name = 'Test' or getenv('NODE_NAME')
this_node_address = 'http://localhost:5000' or getenv('NODE_ADDRESS')

warehouse = Warehouse()
client = HTTPClient()
myself = Node(this_node_name, this_node_address, client)
ring = Ring([myself])

app = Flask(__name__)


@app.get('/keys/<key>')
def read(key):
    if bool(request.args.get('recursive')):
        nodes = ring.get(object(key), replicas=1)
        for node in nodes:
            return node.read(key)
    else:
        return warehouse.read(key)


@app.post('/keys/<key>')
def create(key):
    if bool(request.args.get('recursive')) and bool(request.args.get('replicas')):
        nodes = ring.get(object(key), int(request.args.get('replicas')))
        for node in nodes:
            node.set(key, request.json['value'])
    else:
        warehouse.set(key, request.json['value'])
    return '', 200


@app.delete('/keys/<key>')
def delete(key):
    if bool(request.args.get('recursive')):
        for node in ring.get_all():
            node.unset(key)
    else:
        warehouse.unset(key)
    return '', 200


if __name__ == "__main__":
    app.run(debug=True)
