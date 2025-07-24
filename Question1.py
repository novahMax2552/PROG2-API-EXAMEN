from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.get("/hello")

def helloWorld():
    raise HTTPException (status_code=200, detail="Hello World")