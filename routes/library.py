import fastapi

from services import books_service

router = fastapi.APIRouter()


@router.get('/books')
async def books_get():
    books = await books_service.get_books()
    return books
