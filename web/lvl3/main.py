from flask import Flask, request
import os

app = Flask(__name__)

def open_file(filename):
    with open(filename, 'r') as f:
        return f.read()

@app.route("/")
def home():
    return open_file("html/index.html")

@app.route("/tools", methods=["GET", "POST"])
def flag():
    file = open_file("html/tools.html")
    if request.method == "GET":
        return file.replace("{OUTPUT}", '')
    else:
        if not request.form.get('ip'):
            return file.replace("{OUTPUT}", '')
        # vuln
        os.system(f"ping -c 4 {request.form.get('ip')} > html/out.txt")
        #
        comm = open_file("html/out.txt")
        os.remove("html/out.txt")
        return file.replace("{OUTPUT}", comm.replace('\n', '<br>'))

app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=False)