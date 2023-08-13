from cs50 import SQL
from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)

db = SQL("sqlite:///registrants.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



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




@app.route("/user")
def user():
    if not session.get("name"):
        return redirect("/login")
    return render_template("user.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/user")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/user")

