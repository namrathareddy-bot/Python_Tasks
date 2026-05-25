# ============================================================
# server.py
# (FastAPI APIs / Back-End)
# ============================================================

from fastapi import FastAPI

app = FastAPI()

# ------------------------------------------------------------
# Sample Database
# ------------------------------------------------------------
books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John",
        "available": True
    }
]


# ------------------------------------------------------------
# Home API
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "Library API Running"}


# ------------------------------------------------------------
# Get All Books
# ------------------------------------------------------------
@app.get("/books")
def get_books():
    return books


# ------------------------------------------------------------
# Get Book By ID
# ------------------------------------------------------------
@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:

        if book["id"] == book_id:
            return book

    return {"message": "Book not found"}


# ------------------------------------------------------------
# Add New Book
# ------------------------------------------------------------
@app.post("/books")
def add_book(book: dict):

    books.append(book)

    return {
        "message": "Book added successfully",
        "book": book
    }


# ------------------------------------------------------------
# Update Book
# ------------------------------------------------------------
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):

    for book in books:

        if book["id"] == book_id:

            book.update(updated_book)

            return {
                "message": "Book updated successfully",
                "book": book
            }

    return {"message": "Book not found"}


# ------------------------------------------------------------
# Delete Book
# ------------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            return {"message": "Book deleted successfully"}

    return {"message": "Book not found"}
