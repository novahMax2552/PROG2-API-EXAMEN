from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/hello", responses=str)

def helloWorld():
    print ("Hello World")
    raise HTTPException(status_code=200)