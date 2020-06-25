from flask import Flask, render_template
app = Flask(__name__,)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/home")
def home_handler():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return "This is the signup page"

@app.route("/login")
def login():
    return "This is the login page"

@app.route("/about")
def about():   
    return "This is the about page"