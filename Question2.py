from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/welcome/{name}")

def Welcome(name: str):
    return ("Welcome " + name)