from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = SQL("sqlite:///registrants.db")


SPORTS = [
    "futebol", 
    "volei", 
    "basquete"
]

@app.route("/")
def index():
    return render_template("index.html", sports = SPORTS)


    
@app.route("/register", methods=["POST"])
def register():
    
    name = request.form.get("name")
    if not name:
        return render_template("error.html", mensage="Name missing")
    
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    
    db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name, sport)
            
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)



@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")



