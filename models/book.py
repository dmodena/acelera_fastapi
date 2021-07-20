from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    number_of_pages: int
    published_year: int
