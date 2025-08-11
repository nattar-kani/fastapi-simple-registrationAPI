from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, constr
from fastapi import HTTPException

app = FastAPI()

class validate(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)

regUsers = []

@app.post("/register")
def registerUser(user: validate):
    if any(u['email'] == user.email for u in regUsers):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    regUsers.append(
        {
            "name": user.name,
            "email": user.email,
            "password": user.password
        }
    )

    return {"message": "User registered successfully"}

@app.get("/showUsers")
def userList():
    return [{"username": u["name"], "emailID": u["email"]} for u in regUsers]