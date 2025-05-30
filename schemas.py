from pydantic import BaseModel,EmailStr
#from database import datetime
from typing import Optional

class StudentBase(BaseModel):
    name: str
    sclass: str
    section: str


class StudentCreate(StudentBase):
    pass


class Stu(StudentBase):
    name: str
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    id: int
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr

    class Config:
        orm_modev= True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None