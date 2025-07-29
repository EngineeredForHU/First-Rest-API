# 🧩 My First REST API with Flask

This project is my first attempt at creating a RESTful API using **Python** and the **Flask** web framework. It simulates a basic e-commerce backend where users can create stores and add items to them. This project helped me understand how APIs work, how to handle HTTP requests, and how to structure backend logic using Flask.

---

## 🔍 Project Description

The API supports the following features:

- Create a new store
- Retrieve a list of all stores
- Get a specific store by name
- Add an item to a specific store
- View all items in a specific store

All data is stored in memory (a list of dictionaries), making this a great lightweight starting point for learning.

---

## 🧪 API Endpoints

Here are the main endpoints included in the project:

| Method | Endpoint                     | Description                        |
|--------|------------------------------|------------------------------------|
| GET    | `/store`                     | Get all stores                     |
| POST   | `/store`                     | Create a new store                 |
| GET    | `/store/<name>`              | Get a store by its name            |
| POST   | `/store/<name>/item`         | Add an item to a specific store    |

### Example Store JSON:
```json
{
  "name": "Tech Store"
}
