from fastapi import FastAPI, HTTPException, Response, Depends,status,APIRouter
from sqlalchemy.orm import Session
from typing import Optional,List

from .. import models,schemas,utils,oauth2
from .. database import engine, get_db

router= APIRouter(
    tags=["students"]
)

@router.get("/testconn")
def loadAll(db: Session = Depends(get_db)):
    return {"status": "success"}


@router.get("/loaddemo",response_model=List[schemas.Stu])
def loadAll(db: Session = Depends(get_db)):
    posts = db.query(models.Student).all()
    print(posts)
    return posts

@router.get("/loadall/{name}")
def loadByName(name:str, db: Session = Depends(get_db)):
    post=db.query(models.Student).filter(models.Student.name == name).first()
    print(post)
    return {"data" : post}

@router.delete("/deletepost/{name}")
def loadByName(name:str, db: Session = Depends(get_db)):
    post=db.query(models.Student).filter(models.Student.name == name)
    if post.first() ==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {"message":"user deleted"}
    

@router.post("/create",status_code=status.HTTP_201_CREATED,response_model=schemas.Stu)
def create_post(student:schemas.StudentCreate,db: Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
   
    print(current_user.email)
    new_post= models.Student(**student.dict())
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post





@router.put("/updatepost/{name}")
def update_post(name:str,newstudent:schemas.Stu,db: Session=Depends(get_db)):

    update_post= db.query(models.Stu).filter(models.Student.name == name)

    student=update_post.first()

    if student == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found")
    update_post.update(newstudent.dict(),synchronize_session=False)
    db.commit()
    return{"data":update_post.first()}
