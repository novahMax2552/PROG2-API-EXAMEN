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

@app.put("/students/{student_reference}", response_model=Students)
def update_students(student_reference: str, updated_student: Students):
    students = read_student()
    for i, student in enumerate(students):
        if student.reference == student_reference:
            students[i] = updated_student
            write_student(students)
            return updated_student