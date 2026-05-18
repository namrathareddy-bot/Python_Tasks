# pip install fastapi uvicorn pymysql sqlalchemy

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# MySQL connection
DATABASE_URL = "mysql+pymysql://root:Nikky%402004@localhost:3306/library_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Database table
class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, unique=True, index=True)
    title = Column(String(100))
    author = Column(String(100))
    issued = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# Input model
class Book(BaseModel):
    book_id: int
    title: str
    author: str
    issued: bool = False

@app.get("/")
def home():
    return {"message": "Library Management MySQL API is running"}

@app.post("/books")
def add_book(book: Book):
    db = SessionLocal()

    old_book = db.query(BookDB).filter(BookDB.book_id == book.book_id).first()
    if old_book:
        db.close()
        raise HTTPException(status_code=400, detail="Book already exists")

    new_book = BookDB(
        book_id=book.book_id,
        title=book.title,
        author=book.author,
        issued=book.issued
    )

    db.add(new_book)
    db.commit()
    db.close()

    return {"message": "Book added successfully"}

@app.get("/books")
def get_books():
    db = SessionLocal()
    books = db.query(BookDB).all()
    db.close()
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.book_id == book_id).first()
    db.close()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    db = SessionLocal()
    old_book = db.query(BookDB).filter(BookDB.book_id == book_id).first()

    if not old_book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")

    old_book.title = book.title
    old_book.author = book.author
    old_book.issued = book.issued

    db.commit()
    db.close()

    return {"message": "Book updated successfully"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.book_id == book_id).first()

    if not book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    db.close()

    return {"message": "Book deleted successfully"}

@app.post("/issue-book/{book_id}")
def issue_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.book_id == book_id).first()

    if not book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")

    if book.issued:
        db.close()
        raise HTTPException(status_code=400, detail="Book already issued")

    book.issued = True
    db.commit()
    db.close()

    return {"message": "Book issued successfully"}

@app.post("/return-book/{book_id}")
def return_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.book_id == book_id).first()

    if not book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")

    if not book.issued:
        db.close()
        raise HTTPException(status_code=400, detail="Book is not issued")

    book.issued = False
    db.commit()
    db.close()

    return {"message": "Book returned successfully"}

@app.get("/available-books")
def available_books():
    db = SessionLocal()
    books = db.query(BookDB).filter(BookDB.issued == False).all()
    db.close()
    return books

@app.get("/issued-books")
def issued_books():
    db = SessionLocal()
    books = db.query(BookDB).filter(BookDB.issued == True).all()
    db.close()
    return books

@app.get("/search-book/{title}")
def search_book(title: str):
    db = SessionLocal()
    books = db.query(BookDB).filter(BookDB.title.like(f"%{title}%")).all()
    db.close()
    return books
