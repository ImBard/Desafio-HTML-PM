from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato")
def cont():
    return render_template("contato.html")

@app.route("/who")
def who():
    return render_template("who.html")