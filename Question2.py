from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Welcome(BaseModel):
    name: str


@app.post("/welcome")
def welcome_user(request: Welcome):
    return {f"Welcome {request.name}"}