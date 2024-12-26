from sqlmodel import SQLModel,Column,Field
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime


class User(SQLModel,table=True):
    __tablename__ = 'users'
    uid: uuid.uuid4 = Field(sa_column=Column(pg.UUID,nullable=False,primary_key=True,default=uuid.uuid4))
    username: str = Field(sa_column=Column(pg.VARCHAR,nullable=False,unique=True))
    email: str = Field(sa_column=Column(pg.VARCHAR,nullable=False,unique=True))
    password_hash: str = Field(exclude=True)
    role: str
    is_verified: bool = False
    is_active: bool = False
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP))

