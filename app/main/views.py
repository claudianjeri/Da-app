from . import main

@main.route('/')
def index():
    return '<h1> Hello You </h1>'

