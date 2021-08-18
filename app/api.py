from fastapi import FastAPI
from .database import save_todo, get_todo, get_todos, update_todo, remove_todo

app = FastAPI()

@app.get("/")
def welcome():
    return {
        "message": "Hello from Okteto's developer community!"
    }

@app.post("/todo")
def add_todo(item: dict):
    data = save_todo(item)
    return data

@app.get("/todo/{id}")
def retrieve_todo(id: str):
    return get_todo(id)

@app.get("/todo")
def retrieve_todos():
    return get_todos()

@app.put("/todo/{id}")
def update_todo_data(id: str, item: dict):
    updated_todo = update_todo(id, item)
    if updated_todo:
        return {
            "message": "Todo updated successfully"
        }
    return {
        "error": "There was an error updating your todo"
    }

@app.delete("/todo/{id}")
def delete_todo(id: str):
    deleted_todo = remove_todo(id)
    if deleted_todo:
        return {
            "message": "Todo deleted successfully"
        }
    return {
        "error": "There was an error deleting your todo."
    }
