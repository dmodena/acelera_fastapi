import fastapi

router = fastapi.APIRouter()


class Book:
    def __init__(self, title, author, number_of_pages, published_year):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.published_year = published_year


__books = [
    Book('Os Próprios Deuses', 'Isaac Asimov', '301', '2001'),
    Book('Duna', 'Frank Herbert', '470', '2005')
]


@router.get('/books')
def books_get():
    return __books
