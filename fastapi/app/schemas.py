from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class UserStruct(BaseModel):
    email : EmailStr
    password : str

class CreateUser(UserStruct):
    pass

class User(BaseModel):
    id : int
    email : EmailStr
    createdAt : datetime
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class PostStruct(BaseModel):
    title: str
    content: str

class CreatePost(PostStruct):
    pass

class Post(BaseModel):
    id : int
    title: str
    content: str
    published: bool
    createdAt: datetime
    user_id: int
    owner : User
    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id : int
    dir : conint(ge=0,le=1)