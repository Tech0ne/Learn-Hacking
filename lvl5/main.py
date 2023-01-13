from flask import Flask, request, make_response
import base64, pickle

app = Flask(__name__)

def open_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return "File not found !"

class main:
    def __init__(self, string):
        self.string = string
    def __repr__(self):
        return self.string
    def __str__(self):
        return self.string

@app.route("/")
def home():
    cookie = request.cookies.get("data_to_show")
    if not cookie:
        cookie = "gASVWQAAAAAAAACMCF9fbWFpbl9flIwEbWFpbpSTlCmBlH2UjAZzdHJpbmeUjDFUaGlzIGlzIGp1c3Qgc29tZSBkYXRhIHNhdmVkIGJ5IHNvbWUgdW5jb21vbiB3YXlzlHNiLg=="
    try:
        dcoded = base64.b64decode(cookie.encode())
        output = str(pickle.loads(dcoded))
    except Exception as e:
        output = "Error ! (" + str(e) + ")"
    resp = make_response(open_file("html/index.html").replace("{OUTPUT}", output))
    resp.set_cookie("data_to_show", value=cookie)
    return resp

app.run(host="0.0.0.0", port=__import__('os').getenv("PORT"), debug=False)