from pydantic import BaseModel, Field, EmailStr
from typing import List

class UserSchema(BaseModel):
  fullname : str = Field(default = None)
  email : EmailStr = Field(default = None)
  password : str = Field(default = None)
  class Config:
    the_schema = {
        "user_demo": {
          "name" : "Ed",
          "email" : "elremolino91@gmail.com",
          "password" : "123"
        }
    }

class UserLoginSchema(BaseModel):
  email : EmailStr = Field(default = None)
  password : str = Field(default = None)
  class Config:
    the_schema = {
        "user_demo": {
          "email" : "elremolino91@gmail.com",
          "password" : "123"
        }
    }

class PokemonTeam(BaseModel):
  team : list[int] = None




