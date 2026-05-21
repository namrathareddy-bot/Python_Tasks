from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField, BooleanField

# ------------------------------------------------------------
# FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# MongoDB Connection
# ------------------------------------------------------------
connect(
    db="library_db",
    host="mongodb+srv://namrathareddy816_db_user:<db_password>@cluster0.udiakhx.mongodb.net/?appName=Cluster0"
)
# ------------------------------------------------------------
# MongoDB Model
# ------------------------------------------------------------
class BookDB(Document):
    book_id = IntField(required=True, unique=True)
    title = StringField(required=True)
    author = StringField(required=True)
    issued = BooleanField(default=False)

# ------------------------------------------------------------
# Pydantic Model
# ------------------------------------------------------------
class Book(BaseModel):
    book_id: int
    title: str
    author: str
    issued: bool = False

# ------------------------------------------------------------
# Home API
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "Library Management API is running"}

# ------------------------------------------------------------
# Add Book
# ------------------------------------------------------------
@app.post("/books")
def add_book(book: Book):
    old_book = BookDB.objects(book_id=book.book_id).first()

    if old_book:
        raise HTTPException(status_code=400, detail="Book already exists")

    new_book = BookDB(
        book_id=book.book_id,
        title=book.title,
        author=book.author,
        issued=book.issued
    )
    new_book.save()

    return {"message": "Book added successfully"}

# ------------------------------------------------------------
# Get All Books
# ------------------------------------------------------------
@app.get("/books")
def get_books():
    books = BookDB.objects()

    return [
        {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "issued": book.issued
        }
        for book in books
    ]

# ------------------------------------------------------------
# Get Book by ID
# ------------------------------------------------------------
@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = BookDB.objects(book_id=book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "book_id": book.book_id,
        "title": book.title,
        "author": book.author,
        "issued": book.issued
    }

# ------------------------------------------------------------
# Update Book
# ------------------------------------------------------------
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    old_book = BookDB.objects(book_id=book_id).first()

    if not old_book:
        raise HTTPException(status_code=404, detail="Book not found")

    old_book.title = book.title
    old_book.author = book.author
    old_book.issued = book.issued
    old_book.save()

    return {"message": "Book updated successfully"}

# ------------------------------------------------------------
# Delete Book
# ------------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = BookDB.objects(book_id=book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.delete()

    return {"message": "Book deleted successfully"}

# ------------------------------------------------------------
# Issue Book
# ------------------------------------------------------------
@app.post("/issue-book/{book_id}")
def issue_book(book_id: int):
    book = BookDB.objects(book_id=book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.issued:
        raise HTTPException(status_code=400, detail="Book already issued")

    book.issued = True
    book.save()

    return {"message": "Book issued successfully"}

# ------------------------------------------------------------
# Return Book
# ------------------------------------------------------------
@app.post("/return-book/{book_id}")
def return_book(book_id: int):
    book = BookDB.objects(book_id=book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if not book.issued:
        raise HTTPException(status_code=400, detail="Book is not issued")

    book.issued = False
    book.save()

    return {"message": "Book returned successfully"}

# ------------------------------------------------------------
# Available Books
# ------------------------------------------------------------
@app.get("/available-books")
def available_books():
    books = BookDB.objects(issued=False)

    return [
        {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "issued": book.issued
        }
        for book in books
    ]

# ------------------------------------------------------------
# Issued Books
# ------------------------------------------------------------
@app.get("/issued-books")
def issued_books():
    books = BookDB.objects(issued=True)

    return [
        {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "issued": book.issued
        }
        for book in books
    ]

# ------------------------------------------------------------
# Search Book by Title
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(title: str):
    books = BookDB.objects(title__icontains=title)

    return [
        {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "issued": book.issued
        }
        for book in books
    ]

