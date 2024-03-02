from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import SessionLocal
from jose import JWTError, jwt
from utils.password import verify_password
from crud import user as userCrud

router = APIRouter()

SECRET_KEY = "705a71d401e528e5c9b73f2d34f7644eec187af1985a45b42f636ef412319351"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user_dict = userCrud.get_user_by_email(db, form_data.username)

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(form_data.password, user_dict.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user_dict.email, "token_type": "bearer"}