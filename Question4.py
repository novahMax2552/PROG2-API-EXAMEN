from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

@app.post("/students")

class Students(BaseModel):
    reference: str
    FirstName: str
    Lastname: str
    Age: int

DB_FILE = "students.json"

def read_student() -> List[Students]:
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        data = json.load(f)
        return [Students(**item) for item in data]

def write_student(students: List[Students]):
    with open(DB_FILE, "w") as f:
        json.dump([student.dict() for student in students], f, indent=4)

@app.get("/students", response_model=List[Students])
def get_students():
    return read_student()