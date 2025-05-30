from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP,DateTime
from .database import Base

class Student(Base):
    __tablename__="STUDENT"

    name=Column(String,primary_key=True,nullable=False)
    sclass=Column(String,nullable=False)
    section=Column(String,nullable=False)
    #createdat=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class User(Base):
    __tablename__="users"
    id= Column(Integer, primary_key=True, nullable=False)
    email=Column(String,primary_key=True,nullable=False)
    password=Column(String,nullable=False)


