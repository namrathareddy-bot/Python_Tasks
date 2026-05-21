from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

# -----------------------------------
# Home Page Route
# -----------------------------------
@app.route("/")
def home_page():

    # Open index.html page
    return render_template("index.html")

# -----------------------------------
# Second Page Route
# -----------------------------------
@app.route("/second")
def second_page():

    # Open second.html page
    return render_template("second.html")

# -----------------------------------
# Run Flask Server
# -----------------------------------
if __name__ == "__main__":

    # Start application in debug mode
    app.run(debug=True)
