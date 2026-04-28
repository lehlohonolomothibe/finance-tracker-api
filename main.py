from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

from fastapi import HTTPException

fake_user = {
    "username": "admin",
    "password": "1234"
}

@app.post("/login")
def login(username: str, password: str):
    if username == fake_user["username"] and password == fake_user["password"]:
        return {"message": "login success"}
    raise HTTPException(status_code=401, detail="invalid credentials")