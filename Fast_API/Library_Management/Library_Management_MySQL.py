# =====================================================================================
# 📚 FastAPI Library Management System (MySQL + 3 Tables)
# =====================================================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# =====================================================================================
# 🚀 FastAPI App
# =====================================================================================

app = FastAPI()

# =====================================================================================
# 🗄️ MySQL Connection
# =====================================================================================

DATABASE_URL = "mysql+pymysql://root:root123@localhost/library_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# =====================================================================================
# 📚 TABLE 1 → BOOKS
# =====================================================================================

class BooksDB(Base):

    __tablename__ = "Books"

    book_id = Column(Integer, primary_key=True)

    title = Column(String(255))

    genre = Column(String(255))

    author = Column(String(255))

    price = Column(Float)

    available = Column(Boolean, default=True)

# =====================================================================================
# 👤 TABLE 2 → USERS
# =====================================================================================

class UsersDB(Base):

    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True)

    username = Column(String(255))

    email = Column(String(255))

    phone = Column(String(20))

# =====================================================================================
# 📖 TABLE 3 → ISSUED BOOKS
# =====================================================================================

class IssuedBooksDB(Base):

    __tablename__ = "Issued_Books"

    issue_id = Column(Integer, primary_key=True, autoincrement=True)

    book_id = Column(Integer, ForeignKey("Books.book_id"))

    user_id = Column(Integer, ForeignKey("Users.user_id"))

# =====================================================================================
# ✅ CREATE TABLES
# =====================================================================================

Base.metadata.create_all(bind=engine)

# =====================================================================================
# 🧾 PYDANTIC MODELS
# =====================================================================================

class Book(BaseModel):

    book_id: int
    title: str
    genre: str
    author: str
    price: float
    available: bool = True

class User(BaseModel):

    user_id: int
    username: str
    email: str
    phone: str

class IssueBook(BaseModel):

    book_id: int
    user_id: int

# =====================================================================================
# 🔌 DATABASE SESSION
# =====================================================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# =====================================================================================
# 🏠 HOME API
# =====================================================================================

@app.get("/")
def home():

    return {"message": "Library Management System Running"}

# =====================================================================================
# 📚 BOOK APIs
# =====================================================================================

# -------------------------------------------------
# ➕ ADD BOOK
# -------------------------------------------------

@app.post("/books")
def add_book(book: Book, db: Session = Depends(get_db)):

    existing = db.query(BooksDB).filter(
        BooksDB.book_id == book.book_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Book already exists"
        )

    new_book = BooksDB(
        book_id = book.book_id,
        title = book.title,
        genre = book.genre,
        author = book.author,
        price = book.price,
        available = book.available
    )

    db.add(new_book)

    db.commit()

    db.refresh(new_book)

    return {
        "message": "Book Added Successfully",
        "data": new_book
    }

# -------------------------------------------------
# 📖 GET ALL BOOKS
# -------------------------------------------------

@app.get("/books")
def get_books(db: Session = Depends(get_db)):

    books = db.query(BooksDB).all()

    return {
        "count": len(books),
        "data": books
    }

# -------------------------------------------------
# 🔍 GET SINGLE BOOK
# -------------------------------------------------

@app.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(BooksDB).filter(
        BooksDB.book_id == book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book

# -------------------------------------------------
# ✏️ UPDATE BOOK
# -------------------------------------------------

@app.put("/books/{book_id}")
def update_book(book_id: int, updated: Book, db: Session = Depends(get_db)):

    book = db.query(BooksDB).filter(
        BooksDB.book_id == book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.title = updated.title
    book.genre = updated.genre
    book.author = updated.author
    book.price = updated.price
    book.available = updated.available

    db.commit()

    db.refresh(book)

    return {
        "message": "Book Updated Successfully",
        "data": book
    }

# -------------------------------------------------
# ❌ DELETE BOOK
# -------------------------------------------------

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(BooksDB).filter(
        BooksDB.book_id == book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)

    db.commit()

    return {"message": "Book Deleted Successfully"}

# =====================================================================================
# 👤 USER APIs
# =====================================================================================

# -------------------------------------------------
# ➕ ADD USER
# -------------------------------------------------

@app.post("/users")
def add_user(user: User, db: Session = Depends(get_db)):

    existing = db.query(UsersDB).filter(
        UsersDB.user_id == user.user_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = UsersDB(
        user_id = user.user_id,
        username = user.username,
        email = user.email,
        phone = user.phone
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User Added Successfully",
        "data": new_user
    }

# -------------------------------------------------
# 👥 GET USERS
# -------------------------------------------------

@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(UsersDB).all()

    return {
        "count": len(users),
        "data": users
    }

# =====================================================================================
# 📖 ISSUE BOOK APIs
# =====================================================================================

# -------------------------------------------------
# 📕 ISSUE BOOK
# -------------------------------------------------

@app.post("/issue-book")
def issue_book(data: IssueBook, db: Session = Depends(get_db)):

    book = db.query(BooksDB).filter(
        BooksDB.book_id == data.book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if not book.available:
        raise HTTPException(
            status_code=400,
            detail="Book already issued"
        )

    user = db.query(UsersDB).filter(
        UsersDB.user_id == data.user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    issue = IssuedBooksDB(
        book_id = data.book_id,
        user_id = data.user_id
    )

    book.available = False

    db.add(issue)

    db.commit()

    return {"message": "Book Issued Successfully"}

# -------------------------------------------------
# 📚 VIEW ISSUED BOOKS
# -------------------------------------------------

@app.get("/issued-books")
def issued_books(db: Session = Depends(get_db)):

    books = db.query(IssuedBooksDB).all()

    return {
        "count": len(books),
        "data": books
    }

# -------------------------------------------------
# 🔄 RETURN BOOK
# -------------------------------------------------

@app.put("/return-book/{book_id}")
def return_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(BooksDB).filter(
        BooksDB.book_id == book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.available = True

    db.commit()

    return {"message": "Book Returned Successfully"}
