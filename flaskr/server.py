from flask import Flask
import json

app = Flask(__name__)
import Item

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getItems")
def getItems():
    items = []
    items.append(Item(14253223, 231, name='salt'))

    return json.dumps(items)