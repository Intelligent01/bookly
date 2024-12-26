from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from pydantic import EmailStr
from datetime import datetime
import uuid


class Book(SQLModel,table = True):
    __tablename__ = 'books'
    uid: uuid.UUID = Field(
        sa_column= Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    id: int = Field(
        sa_column= Column(
            pg.INTEGER,
            nullable=False,
            unique=True,)
    )
    publisher: str
    published_date: str = Field(sa_column = Column(pg.DATE))
    title: str
    age: int
    phone: str
    email: EmailStr
    created_at: datetime = Field(sa_column = Column(pg.TIMESTAMP,default=datetime.now))
    updated_at: datetime = Field(sa_column = Column(pg.TIMESTAMP,default=datetime.now))

    def __repr__(self):
        return f'<Book {self.name} >'
    

    
# class updateBook(SQLModel):
    
#     publisher: str
#     title: str
#     age: int
#     phone: str
#     email: EmailStr

