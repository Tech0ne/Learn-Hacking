from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_file(open("main.pcapng", 'rb'), download_name="main")

app.run(host="0.0.0.0", port=int(os.getenv("PORT")), debug=False)
