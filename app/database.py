from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://mongodb:27017")

db = client.crud

crud_coll = db.get_collection("crud")


def parse_todo(todo):
    return {
        "id": str(todo["_id"]),
        "item": todo["item"]
    }

def save_todo(todo: dict) -> dict:
    saved_todo = crud_coll.insert_one(todo).inserted_id

    return {
        "id": str(saved_todo)
    }

def get_todo(id: str):
    todo = crud_coll.find_one({"_id": ObjectId(id)})

    return {
        "item": todo["item"]
    }

def get_todos():
    todos = []
    for todo in crud_coll.find():
        todos.append(parse_todo(todo))
    return {
        "todos": todos
    }

def update_todo(id: str, item: dict):
    todo = crud_coll.find_one({"_id": ObjectId(id)})
    if todo:
        crud_coll.update_one({"_id": ObjectId(id)}, {"$set": item})
        return True

def remove_todo(id: str):
    todo = crud_coll.find_one({"_id": ObjectId(id)})
    if todo:
        crud_coll.delete_one({"_id": ObjectId(id)})
        return True