from fastapi import FastAPI
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from models import itemModel, userModel
from routes import items, users, auth
from crud import user

itemModel.Base.metadata.create_all(bind=engine)
userModel.Base.metadata.create_all(bind=engine)



app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# /users/ and /items/ routes
# ======================

app.include_router(users.router)
app.include_router(items.router)
app.include_router(auth.router)