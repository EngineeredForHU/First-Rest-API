from flask import Flask, request

app = Flask(__name__)


stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }

]

# the end point is the /store
@app.get("/store")
def get_store():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "item":[]}
    stores.append(new_store)
    return new_store, 201
    # Status code for view function is 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"],"price": request_data["price"]}
            store["items"].append(new_item)
            return new_item,201
    return {"message": "store not found"}, 404
    # Status code for view function is 404


@app.get("/store/<string:name>")
def get_storew(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"Message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"]== name:
            return {"items": store["items"]}
    return {"Message": "Store not found"}, 404

if __name__ == '__main__':
    app.run()
