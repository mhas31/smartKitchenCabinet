import os
import json
from flask import Flask, g
from flask.templating import render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import Item
    from . import ItemTracker
    from . import weightSensor


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/getItems")
    def getItems():
        items = []
        ite = Item.Item(14253223, 231, name='salt')
        ite2 = Item.Item(13653443, 123, name='sugar')
        items.append(ite)
        items.append(ite2)
        wSensor = weightSensor.WeightSensor()

        weights = []

        found = ItemTracker.ItemTracker(0).scan(100)
        weights = wSensor.readLast()



        print(found)

        for (code, location) in found:
            for item in items:
                if int(code) == item.colorCode:
                    item.location = location
        
        for i in range(len(weights)):
            for item in items:
                if i+1 == item.location:
                    item.weight = weights[i]


        g.items = items
        

        itemsdic = [obj.todict() for obj in items]

        js = json.dumps(itemsdic)

        return render_template("allItems.html")

    return app