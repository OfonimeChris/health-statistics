from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__)  #app is the instance of a class

base_path = pathlib.Path().cwd()
db_name = "health_insurrance.db"
file_path = base_path / db_name

@app.route("/")
def index():
    #return "Hello world"
    return render_template("index_fillin.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(file_path) #connect to the database
    cursor = con.cursor()
    health = cursor.execute("SELECT *FROM health").fetchall()
    con.close()
    return render_template("data_table_fillin.html", health=health)

if __name__=="__main__":
    app.run(debug=True)
    
    #return "chi>My Awesome project</>"