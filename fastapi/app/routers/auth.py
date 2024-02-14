from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .. import models,schemas,database,utils, oauth2
from .. database import  get_db

router = APIRouter(
    prefix="/login",
    tags=["Auth"]
)

templates = Jinja2Templates(directory="templates")

@router.post("/", response_model=schemas.Token)
def login_user(user_credentials : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid user")

    if not utils.login( user.password,user_credentials.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
    return {"access_token" : access_token, "token_type" : "bearer"}