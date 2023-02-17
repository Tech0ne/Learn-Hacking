from flask import Flask, send_file
import os

app = Flask(__name__)

def open_file(filename):
    with open(filename, 'r') as f:
        return f.read()

@app.route("/")
def home():
    return open_file("html/index.html")

@app.route("/message")
def message():
    return send_file("./message.txt")

app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=False)