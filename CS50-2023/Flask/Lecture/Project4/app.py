from cs50 import SQL
from flask import Flask, render_template, request

app = Flask("__name__")

db = SQL("sqlite:///shows.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    if q:        
        shows = db.execute("SELECT * FROM shows WHERE Series_Title LIKE ? LIMIT 50", "%" + request.args.get("q") + "%")
    else:
        shows = []
    return render_template("search.html", shows=shows)

