from flask import (
    Flask, 
    request
)
from app.database import task
# REST - Representational State Transfer
# Architectural design pattern for building network connected services
app = Flask(__name__)
# ReSTful systems should consist of:
# 1. Idempotent routes and routines
# 2. Endpoints that use plural nouns for names: /users, /products, /orders,
# 3. HTTP methods should be mapped correctly to the type of operation, so:
# 3.1. POST is for create
# 3.2. GET is for read
# 3.3. PUT/PATCH are for update (complete and partial)
# 3.4. DELETE is for deleting
# 3.5. Remember, scan is another read operation, so that uses GET as well.
@app.get("/")
@app.get("/tasks")
def get_all_task():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>/")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.put("/tasks/<int:pk>/")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>/")
def delete_task(pk):
    task.delete_by_id (pk)
    return "", 204