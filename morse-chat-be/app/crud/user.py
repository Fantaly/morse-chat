from sqlalchemy.orm import Session

#import models, schemas
from models import userModel
from schemas import user
from utils.password import hash_password, verify_password


def get_user(db: Session, user_id: int):
    return db.query(userModel.User).filter(userModel.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(userModel.User).filter(userModel.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(userModel.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user.UserCreate):
    """
    Create a new user in the database.

    Args:
        db (Session): The database session.
        user (UserCreate): The user data to be created.

    Returns:
        User: The created user object.
    """
    real_hashed_password = hash_password(user.password)

    db_user =  userModel.User(email=user.email, hashed_password=real_hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

