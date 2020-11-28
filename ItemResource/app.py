''' this file illustrates the creation of Item Resource REST API using

1. Flask-RESTful - Create , Update , Delete and Display
2. Authentication using Flask-JWT
3. Passing only the essential arguments using reqparse

 '''

from flask import Flask, request
from flask_restful import Api, Resource , reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "guru"
api = Api(app)

# for authentication
jwt = JWT(app, authenticate, identity)  # has endpoint "/auth"

# creating an empty list
items = []


class Item(Resource):
    parser = reqparse.RequestParser() #creating object
    parser.add_argument("price",
                        required = True,
                        type = float,
                        help = "This field cannot be left blank"
                        )


    # for get method / retrieving the data
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item": None}, 200 if item else 404  # if the item is not present in the list. 404 is HTTPS status code for page not found

    # creating a new item
    def post(self, name):
        # if the item already exists.
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"Error": f"The item {name} already exists"}, 400

        # if the item is new
        # taking input
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}  # price value given default
        items.append(item)
        return item, 201  # 201 - is HTTP status code for creating record

    # to delete items
    def delete(self, name):
        global items  # declaring items globally
        items = list(filter(lambda x: x['name'] != name, items))
        return {"Message": "Item deleted....",
                "List of items": items}

    # this method can create new items or update the current item
    def put(self, name):
        data = Item.parser.parse_args()

        # iterating through each items in the list
        item = next(filter(lambda x: x['name'] == name, items), None)

        # to check if the item already exists
        # if it does not exists then create a new item,
        if item is None:
            item = {"name": name, "price": data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


# Resource for getting Item List
class ItemList(Resource):
    def get(self):
        return {'items': items}


# adding the resource in the API
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# running the API
if __name__ == "__main__":
    app.run(debug=True)
