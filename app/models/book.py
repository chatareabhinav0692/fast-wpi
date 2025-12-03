from sqlmodel import SQLModel, Field

class Book(SQLModel, table = True):
    id: int = Field(primary_key= True)
    title: str
    author: str
    year: int
    isbn: int
    available: bool