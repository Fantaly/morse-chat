from pydantic import BaseModel

from db.database import Base

class Token(BaseModel):
    access_token: str
    token_type: str