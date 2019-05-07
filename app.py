from flask import Flask

app = Flask(__name__)

@app.route("/")
def basic_response():
    print("Someone clicked this link!")
    return "This is a Website!"

@app.route("/click/<user>")
def name_response(user):
    print("{} clicked this link!".format(user))
    return "This is a Website!"

app.run()