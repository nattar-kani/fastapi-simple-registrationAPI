from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/nat") #decorator to expose my function
def add(x:int,y:int):
    return x+y

class validate(BaseModel):
    #pydantic helps in data validation here
    x: int
    y: int

def subtract(x,y):
    return x-y

@app.post("/sub")
def subtract2(model: validate):
    return subtract(model.x, model.y)

def multi(x,y):
    return x*y

@app.post("/multiply")
def multi2(model: validate):
    return multi(model.x, model.y)
