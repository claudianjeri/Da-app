from . import main

@main.route('/')
def index():
    return '<h1> Hello Kj </h1>'

