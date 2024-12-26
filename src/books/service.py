from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreate,BookUpdate
from sqlmodel import select,desc
from datetime import datetime
from .models import Book


class BookService:
    async def get_all_books(self,session: AsyncSession):
        stmt = select(Book).order_by(desc(Book.id))
        result = await session.exec(stmt)
        return result.all()

    async def get_book(self,book_id:int,session: AsyncSession,):
        stmt = select(Book).where(Book.id == book_id)
        result = await session.exec(stmt)
        book = result.first()

        return book if book is not None else None
    
    async def create_book(self,book_date: BookCreate , session: AsyncSession):
        book_date_dict = book_date.model_dump()
        print(book_date_dict)
        new_book = Book(**book_date_dict)
        new_book.published_date = datetime.strptime(book_date_dict['published_date'],"%Y-%m-%d")
        session.add(new_book)
        await session.commit()
        return new_book


    async def update_book (self, book_id:str, upadate_date: BookUpdate , session: AsyncSession):
        book_to_update = await self.get_book(book_id,session)

        if book_to_update is not None:
            book_data_dict = upadate_date.model_dump()
            for k,v in book_data_dict.items():
                setattr(book_to_update,k,v)
                
            await session.commit()
            return book_to_update
        else:
            return None

    async def delete_book (self, book_id:int, session: AsyncSession):
        book_to_delete = await self.get_book(book_id,session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return {}
        else:
            return None