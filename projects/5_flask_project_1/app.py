import imp
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello I am Flask!!"

if __name__ == "__main__":
    app.run()    