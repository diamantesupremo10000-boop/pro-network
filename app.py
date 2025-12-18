from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def index():
    db = get_db()
    posts = db.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    db.close()
    return render_template("index.html", posts=posts)

@app.route("/post", methods=["POST"])
def post():
    content = request.form["content"]
    db = get_db()
    db.execute("INSERT INTO posts (content) VALUES (?)", (content,))
    db.commit()
    db.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
