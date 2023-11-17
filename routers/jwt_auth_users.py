from fastapi import FastAPI, Depends, HTTPException,status 
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User (BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB (User):
    password: str
    
users_db = {
    "nahue99": {
        "username": "nahue99",
        "full_name": "Nahuel Andujar",
        "email": "nahuel.andujar@hotmail.com",
        "disable": False,
        "password": "110899"
    },
    "martin00": {
        "username": "martin00",
        "full_name": "Martin Casillo",
        "email": "martin.casillo@hotmail.com",
        "disable": True,
        "password": "290200"
    }
}