import fastapi
import uvicorn
from fastapi import FastAPI, Body
from model import UserSchema, UserLoginSchema
from jwt_handler import signJWT

app = FastAPI()

users = []


@app.get("/", tags=["test"])
def greet():
    return {'hello': 'world'}

# User Signup
@app.post("user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default = None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False