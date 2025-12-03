from sqlmodel import Session, select
from ..models.book import Book

class BookService:
    @staticmethod
    def get_book(book_id: int, session: Session):
        return session.get(Book, book_id)
    
    @staticmethod
    def get_all(session: Session):
        return session.exec(select(Book)).all()
    
    @staticmethod
    def create_book(book: Book, session: Session) -> Book:
        session.add(book)
        session.commit()
        return book
    

    @staticmethod
    def update_book(book: Book, session: Session) -> Book:
        book1 = session.get(Book, book.id)
        book1.author = book.author
        session.add(book1)
        session.commit()
        return None

    @staticmethod
    def delete_book(book_id: int, session: Session) -> bool:
        book = session.get(Book, book_id)
        session.delete(book)
        session.commit()
        return True
