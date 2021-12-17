import uvicorn
from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/", tags=["test"])
def greet():
    return {'hello': 'world'}

