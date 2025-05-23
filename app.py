from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/password_challenge/ex/0.html")
def _0():
    return render_template('0.html')

@app.route("/password_challenge/ex/1.html")
def _1():
    return render_template('1.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)