from flask import Flask, request
import os

app = Flask(__name__)

FLAG = "flag{aefcecef7b8bf2a9b53d0f042a28afec}"

def open_file(filename):
    with open(filename, 'r') as f:
        return f.read()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return open_file("html/index.html").replace("{FLAG}", "")
    else:
        test = request.form.get("passwd")
        if test == "7777777777":
            return open_file("html/index.html").replace("{FLAG}", FLAG)
        else:
            return open_file("html/index.html").replace("{FLAG}", "")

app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=False)