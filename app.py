from flask import Flask, request

app = Flask(__name__)

# In-memory "database" of stores.
# Each store has a name and a list of items (name + price).
stores = [
    {
        # added hardcoded data but "Cookie shop" is through imsomnia JSON
        "name": "My Store",
        "items": [
            {"name": "Chair", "price": 15.99}
        ]
    }
]

# GET /store
# Returns all stores and their items.
@app.get("/store")
def get_store():
    return {"stores": stores}

# POST /store
# Creates a new store.
# Expected JSON body: {"name": "<store_name>"}
@app.post("/store")
def create_store():
    request_data = request.get_json()
    # Create an empty items list for the new store
    new_store = {"name": request_data["name"], "items": []}  # <-- fixed key to "items"
    stores.append(new_store)
    return new_store, 201  # 201 Created

# POST /store/<name>/item
# Adds a new item to an existing store.
# Expected JSON body: {"name": "<item_name>", "price": <number>}
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return new_item, 201  # 201 Created
    # If no store matched the given name, return 404 Not Found
    return {"message": "Store not found"}, 404

# GET /store/<name>
# Returns a single store (including its items) by name.
@app.get("/store/<string:name>")
def get_storew(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

# GET /store/<name>/item
# Returns only the items for the specified store.
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

# Run the development server when executed directly.
if __name__ == '__main__':
    app.run()
