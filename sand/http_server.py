from flask import Flask, make_response
from lock_table import LockTable
from ring import Ring
from node import Node

app = Flask(__name__)

lock_table = LockTable()
ring = Ring([Node('me', 'http://localhost:5000/')])


@app.get('/lock/<key>')
def is_lock(key):
    return '', 200 if lock_table.is_lock(key) else 404


@app.post('/lock/<key>')
def lock(key):
    if not any(node.is_lock(key) for node in ring.get_nodes()):
        lock_table.lock(key)
        return '', 200
    return '', 400


@app.delete('/lock/<key>')
def unlock(key):
    lock_table.unlock(key)
    return '', 200


if __name__ == "__main__":
    app.run(debug=True)
