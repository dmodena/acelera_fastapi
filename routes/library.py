import fastapi

from models.book import Book
from services import books_service

router = fastapi.APIRouter()


@router.get('/books')
async def books_get():
    books = await books_service.get_books()
    return books


@router.post('/books')
async def books_post(book: Book):
    book = await books_service.add_book(book)
    return book
