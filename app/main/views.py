from . import main

@main.route('/')
def index():
    return '<h1> World </h1>'

