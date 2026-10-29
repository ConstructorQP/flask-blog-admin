from flask import Flask, render_template, request, redirect
import os
import sqlite3

app = Flask(__name__)
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog.db")


def init_db():
    """Crea la tabla de entradas si no existe y añade una entrada de ejemplo."""
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS entradas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        fecha TEXT,
        autor TEXT,
        contenido TEXT
    )""")
    if cur.execute("SELECT COUNT(*) FROM entradas").fetchone()[0] == 0:
        cur.execute("INSERT INTO entradas (titulo, fecha, autor, contenido) VALUES (?, ?, ?, ?)",
            ("Bienvenido al blog", "2026-03-26", "Hector Quiros",
             "Esta es una entrada de ejemplo. Entra en /admin para crear, editar o borrar entradas."))
    con.commit()
    con.close()


# ---- FRONT PÚBLICO ----

@app.route("/")
def index():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM entradas")
    entradas = cur.fetchall()
    con.close()
    return render_template("index.html", entradas=entradas)

@app.route("/entrada/<int:id>")
def entrada(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM entradas WHERE id=?", (id,))
    entrada = cur.fetchone()
    con.close()
    return render_template("entrada.html", entrada=entrada)


# ---- ADMIN ----

@app.route("/admin")
def admin():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM entradas")
    entradas = cur.fetchall()
    con.close()
    return render_template("admin.html", entradas=entradas)

@app.route("/admin/nueva", methods=["GET", "POST"])
def entrada_nueva():
    if request.method == "POST":
        con = sqlite3.connect(DB)
        cur = con.cursor()
        cur.execute("INSERT INTO entradas (titulo, fecha, autor, contenido) VALUES (?, ?, ?, ?)",
            (request.form["titulo"], request.form["fecha"],
             request.form["autor"], request.form["contenido"]))
        con.commit()
        con.close()
        return redirect("/admin")
    return render_template("entrada_form.html", entrada=None)

@app.route("/admin/editar/<int:id>", methods=["GET", "POST"])
def entrada_editar(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    if request.method == "POST":
        cur.execute("UPDATE entradas SET titulo=?, fecha=?, autor=?, contenido=? WHERE id=?",
            (request.form["titulo"], request.form["fecha"],
             request.form["autor"], request.form["contenido"], id))
        con.commit()
        con.close()
        return redirect("/admin")
    cur.execute("SELECT * FROM entradas WHERE id=?", (id,))
    entrada = cur.fetchone()
    con.close()
    return render_template("entrada_form.html", entrada=entrada)

@app.route("/admin/eliminar/<int:id>")
def entrada_eliminar(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("DELETE FROM entradas WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect("/admin")


# ---- ARRANQUE ----

if __name__ == "__main__":
    init_db()
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")