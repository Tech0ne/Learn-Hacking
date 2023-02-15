from flask import Flask, request, redirect
import os

app = Flask(__name__)

def open_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return "File not found !"

@app.route("/")
def home():
    return open_file("html/index.html")

@app.route("/readme")
def readme():
    if not request.args.get("file"):
        return redirect("/readme?file=some-data.txt")
    return open_file(request.args.get("file"))

# I renamed the flag file to flags.data, they will never know, hehehe

app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=False)
