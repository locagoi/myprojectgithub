from flask import Flask, render_template, redirect, url_for
from OpenSSL import SSL

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

app.run(ssl_context=(../pki/tls/certs))
