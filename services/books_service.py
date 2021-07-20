from models.book import Book

book1 = {
    'title': 'Os Próprios Deuses',
    'author': 'Isaac Asimov',
    'number_of_pages': '301',
    'published_year': '2001'
}

book2 = {
    'title': 'Duna',
    'author': 'Frank Herbert',
    'number_of_pages': 470,
    'published_year': 2005
}

__books = [
    Book(**book1),
    Book(**book2)
]


async def get_books():
    # await some resource
    return __books


async def add_book(book: Book):
    __books.append(book)
    return book
