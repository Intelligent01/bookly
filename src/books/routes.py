from fastapi import APIRouter,status,Header,Depends
from fastapi.exceptions import HTTPException
from .schemas import BookUpdate,Book,BookCreate
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.books.service import BookService
from typing import List

book_router= APIRouter()
book_service = BookService()


@book_router.get('/',response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.get('/{book_id}',response_model=Book)
async def get_book(book_id: int,session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_id,session)
    if book:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no details found")

@book_router.post('/',status_code=status.HTTP_201_CREATED)
async def create_a_books(new_book_data: BookCreate,session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(new_book_data,session)
    return new_book


@book_router.patch('/{book_id}',response_model=Book)
async def update_books(book_id:int,update_book: BookUpdate,session: AsyncSession = Depends(get_session)) -> dict :

    updated_book = await book_service.update_book(book_id,update_book,session)
    if updated_book is not None:
        return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no details found")

@book_router.delete('/{book_id}')
async def delete_book(book_id:int,session: AsyncSession = Depends(get_session)):
    deleted_book = await book_service.delete_book(book_id,session)
    if deleted_book is not None:
        return {"message" : "book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no details found")