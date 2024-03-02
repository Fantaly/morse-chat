from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal

from crud import item
from schemas import item as itemSchema

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/{user_id}/items/", response_model=itemSchema.Item)
def create_item_for_user(user_id: int, item: itemSchema.ItemCreate, db: Session = Depends(get_db)):
    return item.create_user_item(db=db, item=item, user_id=user_id)

@router.get("/items/", response_model=list[itemSchema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item.get_items(db, skip=skip, limit=limit)
    return items