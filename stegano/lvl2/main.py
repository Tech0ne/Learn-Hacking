from flask import Flask, send_file
import os

app = Flask(__name__)

def open_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

@app.route("/")
def home():
    return open_file("html/index.html")

@app.route("/image.png")
def message():
    return open_file("./image.png")

app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=False)