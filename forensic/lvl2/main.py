from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_file(open("somewhere_only_we_know.iso", 'rb'), download_name="somewhere_only_we_know")

app.run(host="0.0.0.0", port=int(os.getenv("PORT")), debug=False)
