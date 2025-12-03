from fastapi import FastAPI, APIRouter
from app.routers.books_router import router as book_router
from app.db.database import init_db 

app = FastAPI()
init_db()

app.include_router(book_router)

@app.get("/")
def root():
    return {"msg": "app started"}