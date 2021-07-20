from models.book import Book

__books = [
    Book('Os Próprios Deuses', 'Isaac Asimov', '301', '2001'),
    Book('Duna', 'Frank Herbert', '470', '2005')
]


def get_books():
    # await some resource
    return __books
