from flask import Flask, render_template, request, redirect
import mysql.connector
from pymongo import MongoClient
import certifi

app = Flask(__name__, template_folder="Templates", static_folder="Static")
# ---------------- MySQL ----------------
mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="library_db"
)

mysql_cursor = mysql_db.cursor(dictionary=True)

# ---------------- MongoDB ----------------
mongo_client = MongoClient(
    "mongodb+srv://namrathareddy816_db_user:Nikky%402004@cluster0.udiakhx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

mongo_db = mongo_client["library_db"]
books_collection = mongo_db["books"]
students_collection = mongo_db["students"]
issued_books_collection = mongo_db["issued_books"]


@app.route("/")
def home():
    return render_template("Index.html")


@app.route("/add-book")
def add_book_page():
    return render_template("Add_Book.html")


@app.route("/books", methods=["POST"])
def add_book():
    book_id = request.form["book_id"]
    title = request.form["title"]
    author = request.form["author"]
    status = "Available"

    mysql_cursor.execute(
        "SELECT * FROM books WHERE book_id = %s",
        (book_id,)
    )
    old_book = mysql_cursor.fetchone()

    if old_book:
        return "Book ID already exists. Please use another Book ID."

    sql = """
    INSERT INTO books (book_id, title, author, status)
    VALUES (%s, %s, %s, %s)
    """

    values = (book_id, title, author, status)

    mysql_cursor.execute(sql, values)
    mysql_db.commit()

    try:
        books_collection.insert_one({
            "book_id": book_id,
            "title": title,
            "author": author,
            "status": status
        })
    except Exception as e:
        print("MongoDB insert error:", e)

    return redirect("/books-page")


@app.route("/books-page")
def books_page():
    mysql_cursor.execute("SELECT * FROM books")
    books = mysql_cursor.fetchall()
    return render_template("Books.html", books=books)


@app.route("/delete-book/<book_id>")
def delete_book(book_id):
    mysql_cursor.execute(
        "DELETE FROM issued_books WHERE book_id = %s",
        (book_id,)
    )

    mysql_cursor.execute(
        "DELETE FROM books WHERE book_id = %s",
        (book_id,)
    )

    mysql_db.commit()

    try:
        books_collection.delete_one({"book_id": book_id})
        issued_books_collection.delete_many({"book_id": book_id})
    except Exception as e:
        print("MongoDB delete error:", e)

    return redirect("/books-page")


@app.route("/students")
def students_page():
    students = [
        {"id": 101, "name": "Abi"},
        {"id": 102, "name": "Amith"},
        {"id": 103, "name": "Lahar"},
        {"id": 104, "name": "Siri"},
        {"id": 105, "name": "Akhil"},
        {"id": 106, "name": "Nikky"}
    ]

    return render_template("Students.html", students=students)


@app.route("/issue-book")
def issue_book_page():
    return render_template("Issue_Book.html")


@app.route("/issue", methods=["POST"])
def issue_book():
    issue_id = request.form["issue_id"]
    book_id = request.form["book_id"]
    member_id = request.form["member_id"]
    issue_date = request.form["issue_date"]
    return_date = request.form["return_date"]

    mysql_cursor.execute(
        "SELECT * FROM issued_books WHERE issue_id = %s",
        (issue_id,)
    )
    old_issue = mysql_cursor.fetchone()

    if old_issue:
        return "Issue ID already exists. Please use another Issue ID."

    sql = """
    INSERT INTO issued_books
    (issue_id, book_id, member_id, issue_date, return_date)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (issue_id, book_id, member_id, issue_date, return_date)

    mysql_cursor.execute(sql, values)

    mysql_cursor.execute(
        "UPDATE books SET status = 'Issued' WHERE book_id = %s",
        (book_id,)
    )

    mysql_db.commit()

    try:
        issued_books_collection.insert_one({
            "issue_id": int(issue_id),
            "book_id": book_id,
            "member_id": int(member_id),
            "issue_date": issue_date,
            "return_date": return_date
        })

        books_collection.update_one(
            {"book_id": book_id},
            {"$set": {"status": "Issued"}}
        )
    except Exception as e:
        print("MongoDB issue error:", e)

    return redirect("/books-page")


@app.route("/return-book")
def return_book_page():
    return render_template("Return_Book.html")


@app.route("/return", methods=["POST"])
def return_book():
    book_id = request.form["book_id"]

    mysql_cursor.execute(
        "UPDATE books SET status = 'Available' WHERE book_id = %s",
        (book_id,)
    )

    mysql_db.commit()

    try:
        books_collection.update_one(
            {"book_id": book_id},
            {"$set": {"status": "Available"}}
        )
    except Exception as e:
        print("MongoDB return error:", e)

    return redirect("/books-page")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/")

    return render_template("Login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            students_collection.insert_one({
                "name": name,
                "email": email,
                "password": password
            })
        except Exception as e:
            print("MongoDB register error:", e)

        return redirect("/login")

    return render_template("Register.html")


if __name__ == "__main__":
    app.run(debug=True, port=5004)