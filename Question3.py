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

def write_student(student: List[Students]):
    with open(DB_FILE, "w") as f:
        json.dump([student.dict() for student in Students], f, indent=4)

@app.post("/students", response_model=Students)
def create_task(student: Students):
    Student = read_student()
    Student.append(student)
    write_student(student)
    return Student