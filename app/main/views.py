from . import main
from flask import Flask,render_template
from flask_bootstrap import Bootstrap



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

