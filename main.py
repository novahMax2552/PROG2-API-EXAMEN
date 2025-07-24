from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI()

# Modèle de tâche
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# Chemin du fichier JSON
DB_FILE = "tasks.json"

# 🔄 Fonctions utilitaires pour lire/écrire le fichier JSON
def read_tasks() -> List[Task]:
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        data = json.load(f)
        return [Task(**item) for item in data]

def write_tasks(tasks: List[Task]):
    with open(DB_FILE, "w") as f:
        json.dump([task.dict() for task in tasks], f, indent=4)

# GET toutes les tâches
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return read_tasks()

# GET une tâche par ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    tasks = read_tasks()
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tâche non trouvée")

# POST créer une tâche
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    return task

# PUT mettre à jour une tâche
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    tasks = read_tasks()
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            write_tasks(tasks)
            return updated_task
    raise HTTPException(status_code=404, detail="Tâche non trouvée")

# DELETE supprimer une tâche
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = read_tasks()
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            write_tasks(tasks)
            return {"message": "Tâche supprimée"}
    raise HTTPException(status_code=404, detail="Tâche non trouvée")
