from fastapi import FastAPI, Response, status, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db, Base
from . import models, schemas
from .routers import post, user, auth, vote

app = FastAPI()
templates = Jinja2Templates(directory="app/template")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root(request : Request):
    return templates.TemplateResponse("index.html" , {"request": request, "name" : "Vanakam da mapla"})
