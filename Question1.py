from fastapi import FastAPI
from starlette.responses import JSONResponse
app = FastAPI()

@app.get("/hello", responses=str)

def helloWorld():
    return JSONResponse({"messages": "Hello world"}, status_code=200)