''' this file demonstrates a simple app to save and retrieve items from a store '''

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Store Dictionary : contains list of dictionaries of stores .
# each store has a list of items in it.
# Each item is a dictionary having its key values as name and price.

stores = [
    {
        "name": "First_Store",
        "items": [
            {
                "name": "Item_1",
                "price": 32.88
            }
        ]
    }
]

# home page
@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
# GET - used to send only data back

''' TO DO :
1. to receive a name of the store and create a record of it.
2. to send the name of the store as a response .
3. to send the list of stores.
4. to receive an item for a specific store with the price details.
5. to send the response containing item and price from the specific store which is asked for.
'''


# 1. to create a  store using POST method giving it a name as given by end user
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()  # takes the data from the json format and converts into python dictionary
    new_store = {
        "name": request_data["name"],  # takes the value from the key"name"
        "items": []  # empty list of items.
    }
    stores.append(new_store)
    return jsonify(new_store)


# 2. to send the name of the store as a response
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over the stores
    # if the name matches return the name else give error
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'Error Description': "Store not found."})


# 3. to send the list of stores.
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})


# 4. to receive an item for a specific store with the price details.
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'Error Description': "Store not found."})



# 5. to send the response containing items list from the specific store which is asked for.
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'Error Description': "Store not found."})


if __name__ == "__main__":
    app.run(debug=True)
