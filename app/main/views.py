from . import main
<<<<<<< HEAD
from flask import render_template

@main.route('/')
def index():
    title = 'Dapp'
    return render_template('index.html', title = title)
=======
from flask import Flask,render_template




@main.route('/')
def index():
    return render_template("index.html")



@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/signup.html")
def signup():
    return render_template("signup.html")

@main.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")

>>>>>>> 654e8660660a240468c234feb3824b736402ad52

