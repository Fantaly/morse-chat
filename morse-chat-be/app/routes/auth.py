from datetime import timedelta, timezone, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, status, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import SessionLocal
from jose import JWTError, jwt
from utils.password import verify_password
from crud import user as userCrud

router = APIRouter()

SECRET_KEY = "705a71d401e528e5c9b73f2d34f7644eec187af1985a45b42f636ef412319351"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

#Example of dict might be {'sub': 'johndoe', 'exp': 1613548570, 'iss': 'http://localhost'}

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    # If expires_delta is not None, then we add an expiration time to the token
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    # Add the expiration time to the token data
    to_encode.update({"exp": expire})

    # Encode the token using the JWT library and our secret key
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

async def get_current_user(request: Request, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Get the token from the cookie
    token = request.cookies.get("access_token")
    if token is None:
        raise credentials_exception

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # payload.get("sub") will return the username of the user, sub stands for subject
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)

    # If the token is invalid, we raise an HTTPException
    except JWTError:
        raise credentials_exception
    
    user = userCrud.get_user_by_email(db, token_data.username)

    if user is None:
        raise credentials_exception
    return user

# This route is used to generate a new token for the user to use in the future requests
# -> Token is the return type of the route
@router.post("/token")
async def login(response: Response, form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> Token:
    user_dict = userCrud.get_user_by_email(db, form_data.username)

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(form_data.password, user_dict.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user_dict.email}, expires_delta=access_token_expires)

    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite="Lax")
    response.status_code = 200
    return response