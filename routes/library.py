import fastapi

from services import books_service

router = fastapi.APIRouter()


@router.get('/books')
def books_get():
    books = books_service.get_books()
    return books
