from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..services.books_service import BookService
from ..db.database import get_session
from ..models.book import Book

router = APIRouter(prefix = "/books")

@router.get("/")
def get_book(book_id: int,session: Session = Depends(get_session)):
    return BookService.get_book(book_id, session)

@router.get("")
def get_all(session: Session = Depends(get_session)):
    return BookService.get_all(session)

@router.post("/")
def create_book(book: Book, session: Session = Depends(get_session)):
    return BookService.create_book(book, session)

@router.put("/")
def update_book(book: Book, session: Session = Depends(get_session)):
    return BookService.update_book(book, session)

@router.delete("/")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    return BookService.delete_book(book_id, session)