from flask import Flask
import os

app = Flask(__name__)

def open_file(filename):
    with open(filename, 'r') as f:
        return f.read()

@app.route("/")
def home():
    return open_file("html/index.html")

@app.route("/flags")
def flag():
    return open_file("html/flag.html")

app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=False)