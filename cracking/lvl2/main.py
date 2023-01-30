from flask import Flask, request
import os

app = Flask(__name__)

FLAG = "flag{49fe81c78a836ce1fe7e01c323842eca}"

def open_file(filename):
    with open(filename, 'r') as f:
        return f.read()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return open_file("html/index.html").replace("{FLAG}", "")
    else:
        test = request.form.get("passwd")
        if test == "montecarlo":
            return open_file("html/index.html").replace("{FLAG}", FLAG)
        else:
            return open_file("html/index.html").replace("{FLAG}", "")

app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=False)