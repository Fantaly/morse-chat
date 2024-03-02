from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import SessionLocal
from utils.password import hash_password, verify_password
from crud import user as userCrud, item as itemCrud
from schemas import user as userSchema, item

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======================
# /users/ route
# Route Description: 
# Create a new user with a hashed password and return the user information
# ======================     
@router.post("/users/", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userCrud.create_user(db=db, user=user)

# ======================
# /users/ and /items/ route
# Route Description:
# Get all users with a limit and offset for pagination purposes
# ======================
@router.get("/users/", response_model=list[userSchema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userCrud.get_users(db, skip=skip, limit=limit)
    return users

# ======================
# /users/{user_id} route
# Route Description: 
# Get a user by user_id and return the user information if found
# ======================
@router.get("/users/{user_id}", response_model=userSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ======================
# /users/{user_id}/items/ route
# Route Description:
# Create an item for a user and return the item information if successful
# ======================
@router.post("/users/{user_id}/items/", response_model=item.Item)
def create_item_for_user(
    user_id: int, item: item.ItemCreate, db: Session = Depends(get_db)
):
    return itemCrud.create_user_item(db=db, item=item, user_id=user_id)


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user_dict = userCrud.get_user_by_email(db, form_data.username)

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(form_data.password, user_dict.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user_dict.email, "token_type": "bearer"}