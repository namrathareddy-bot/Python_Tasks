from flask import Flask, render_template, request, redirect

# ------------------------------------------------
# Create Flask App
# ------------------------------------------------

app = Flask(__name__)

# ------------------------------------------------
# Temporary Database
# ------------------------------------------------

books = []

students = [
    {"id": 1, "name": "Abi", "department": "CSE"},
    {"id": 2, "name": "Siri", "department": "ECE"},
    {"id": 3, "name": "Lahar", "department": "CSE"},
    {"id": 4, "name": "Karthik", "department": "EEE"},
    {"id": 5, "name": "Akhil", "department": "MECH"}
]

# ------------------------------------------------
# Home Page
# ------------------------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# ------------------------------------------------
# View Books
# ------------------------------------------------

@app.route("/books")
def show_books():

    return render_template(
        "books.html",
        books=books
    )


# ------------------------------------------------
# Add Book
# ------------------------------------------------

@app.route("/add-book", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":

        book_id = request.form["book_id"]

        title = request.form["title"]

        author = request.form["author"]

        books.append({
            "book_id": book_id,
            "title": title,
            "author": author,
            "status": "Available"
        })

        return redirect("/books")

    return render_template("add_book.html")


# ------------------------------------------------
# Students Page
# ------------------------------------------------

@app.route("/students")
def students_page():

    return render_template(
        "students.html",
        students=students
    )


# ------------------------------------------------
# Issue Book
# ------------------------------------------------

@app.route("/issue-book", methods=["GET", "POST"])
def issue_book():

    if request.method == "POST":

        book_id = request.form["book_id"]

        for book in books:

            if book["book_id"] == book_id:

                book["status"] = "Issued"

        return redirect("/books")

    return render_template("issue_book.html")


# ------------------------------------------------
# Return Book
# ------------------------------------------------

@app.route("/return-book", methods=["GET", "POST"])
def return_book():

    if request.method == "POST":

        book_id = request.form["book_id"]

        for book in books:

            if book["book_id"] == book_id:

                book["status"] = "Available"

        return redirect("/books")

    return render_template("return_book.html")


# ------------------------------------------------
# Login Page
# ------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        if username == "admin" and password == "admin123":

            message = "Login Successful"

        else:

            message = "Invalid Username or Password"

    return render_template(
        "login.html",
        message=message
    )


# ------------------------------------------------
# Register Page
# ------------------------------------------------

@app.route("/register")
def register():

    return render_template("register.html")


# ------------------------------------------------
# Run Flask App
# ------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)