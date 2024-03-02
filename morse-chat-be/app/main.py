from fastapi import FastAPI
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from db.database import engine
from models import itemModel, userModel
from routes import items, users
from crud import user

itemModel.Base.metadata.create_all(bind=engine)
userModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ======================
# /users/ and /items/ routes
# ======================

app.include_router(users.router)
app.include_router(items.router)