from flask import Flask, render_template
from flask import request
app = Flask(__name__,)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route("/home")
def home_handler():
    return render_template("home.html")


@app.route("/signup",  methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(name, email, password)
        return render_template('signup.html', message="Data Recieved")
    return render_template("/signup.html", message="")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        return render_template('login.html', message="Logged In Sucessfully")
    return render_template("/login.html", message="")


@app.route("/about")
def about():
    return "This is the about page"
