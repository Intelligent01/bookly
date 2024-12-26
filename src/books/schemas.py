from pydantic import BaseModel,EmailStr
from datetime import datetime
import uuid

class Book(BaseModel):
    uid: uuid.UUID
    id: int
    publisher: str
    published_date: str
    title: str
    age: int
    phone: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

class BookCreate(BaseModel):
    id: int
    publisher: str
    published_date: str
    title: str
    age: int
    phone: str
    email: EmailStr


class BookUpdate(BaseModel):
    publisher: str
    title: str
    age: int
    phone: str
    published_date: str
    email: EmailStr
