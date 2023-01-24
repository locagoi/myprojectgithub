from flask import Flask, render_template, redirect, url_for
import os

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/index.html")

@app.route("/projects.html")
def projects():
    return render_template("/projects.html")

@app.route("/team.html")
def team():
    return render_template("/team.html")

@app.route("/services.html")
def services():
    return render_template("/services.html")

@app.route("/contacts.html")
def contacts():
    return render_template("/contacts.html")

@app.route("/index.html")
def index():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(0.0.0.0, debug = True, port = 443, ssl_context = adhoc)

    'context = ('local.crt', 'local.key') #certificate and key files
    'app.run(debug=True, ssl_context=context)

