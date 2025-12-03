from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///.database.db"

engine = create_engine(DATABASE_URL)

def init_db():
    from ..models.book import Book
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session