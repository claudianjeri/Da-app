from . import main

@main.route('/')
def index():
    return '<h1> Hello kirima </h1>'

