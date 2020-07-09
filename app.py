import os
from flask import Flask, render_template
from flask import request
from flask import redirect, url_for
import authentication
import config
app = Flask(__name__,)

# Load config
devEnvironment = os.environ.get('FLASK_ENV')
print("FLASK_ENV = ", devEnvironment)
if devEnvironment == "development":
    app.config.from_object(config.DevelopmentConfig())
elif devEnvironment == "production":
    app.config.from_object(config.ProductionConfig())


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route("/home")
def home_handler():
    return render_template("home.html")


@app.route("/signup",  methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        redirectUrl = url_for('dashboard')
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        authentication.saveUserInfoToFile(
            {'name': name, 'email': email, 'password': password})
        return redirect(redirectUrl)
    return render_template("signup.html", message="")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        emailFlag = authentication.checkEmail(email)
        creditentialsFlag = authentication.checkCredentials(
            {'email': email, 'password': password})
        if emailFlag == False:
            message = "Invalid Email"
        elif emailFlag == True and creditentialsFlag == False:
            message = "Invalid Password"
        elif creditentialsFlag == True:
            redirectUrl = url_for('dashboard')
            message = "Login Successfull"
            return redirect(redirectUrl)
        return render_template('login.html', message=message)
    return render_template("login.html", message="")


@app.route("/about")
def about():
    return "This is the about page"


@app.route("/dashboard")
def dashboard():
    return render_template("/dashboard.html")
