# import libraries
from flask import Flask
from flask_flatpages import FlatPages

# settings for FlatPages
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

# initialize the application
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

# set server name due to development environment restrictions
SERVER_NAME = "0.0.0.0"
SERVER_PORT = 8080

# define the routes
@app.route("/")
def index():
    return "Hello World"

@app.route('/<path:path>/')
def page(path):
    return pages.get_or_404(path).html

if __name__ == "__main__":
    app.run(SERVER_NAME, SERVER_PORT)
