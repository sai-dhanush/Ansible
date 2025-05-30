from operator import index
from typing import Optional,List
from random import randrange
from fastapi import FastAPI, HTTPException, Response, Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from fastapi import status
import sqlite3
from . import models,schemas,utils
from .database import engine, get_db
from .routers import post,user,auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)





