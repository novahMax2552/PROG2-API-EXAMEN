from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/welcome/{name}")



def helloWorld(name: str):
    print ("Welcome" + name)
    raise HTTPException(status_code=200)