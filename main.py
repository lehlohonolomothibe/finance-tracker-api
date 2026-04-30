from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import bcrypt

app = FastAPI()

#stores users
users = {}

# Request models
class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Register endpoint
@app.post("/register")
def register(user: UserRegister):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    users[user.username] = hashed

    return {"message": "user created"}

# Login endpoint
@app.post("/login")
def login(user: UserLogin):
    if user.username not in users:
        raise HTTPException(status_code=400, detail="invalid credentials")

    stored_hash = users[user.username]

    if not bcrypt.checkpw(user.password.encode(), stored_hash):
        raise HTTPException(status_code=401, detail="invalid credentials")

    return {"message": "login success"}