
 
from fastapi import FastAPI, HTTPException, Response, Depends,status,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. database import engine, get_db

from .. import database,schemas,models,utils,oauth2


router= APIRouter(
    tags=["Authetication"]
)

@router.post("/login")
# step-1    
def login(user_cred:schemas.UserLogin,db: Session=Depends(get_db)):
    user= db.query(models.User).filter(models.User.email == user_cred.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    if not utils.verify(user_cred.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}


# step-2
# def login(user_cred:OAuth2PasswordRequestForm=Depends(),db: Session=Depends(database.get_db)):
    
#     user= db.query(models.User).filter(models.User.email == user_cred.email).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
#     if not utils.verify(user_cred.password,user.password):
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
#     access_token=oauth2.create_access_token(data={"user_id":user.id})
#     return {"access_token":access_token,"token_type":"bearer"}