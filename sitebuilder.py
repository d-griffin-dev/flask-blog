from flask import Flask
app = Flask(__name__)

# set server name due to development environment restrictions
SERVER_NAME = "0.0.0.0"
SERVER_PORT = 8080

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(SERVER_NAME, SERVER_PORT)
