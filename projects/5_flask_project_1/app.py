import imp
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello There! I am Flask!!" 

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/user/<int:user_id>")
def user_details(user_id):
    return f"User id: {user_id}"

if __name__ == "__main__":
    app.run(debug=True)    