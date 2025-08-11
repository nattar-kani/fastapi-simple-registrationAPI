from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class validate(BaseModel):
    x: int
    y: int


def multi(x,y):
    return x*y

@app.post("/multiply")
def multi2(model: validate):
    return multi(model.x, model.y)