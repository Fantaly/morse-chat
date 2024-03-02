from sqlalchemy.orm import Session

from models import itemModel
from schemas import item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(itemModel.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: item.ItemCreate, user_id: int):
    db_item = itemModel.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


