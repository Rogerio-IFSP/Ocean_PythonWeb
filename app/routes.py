from app import app
from flask import render_template 


#o @ chama um URL route
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")