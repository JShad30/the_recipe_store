import os
from flask import Flask, render_template

app = Flask(__name__)

"""Rendering the home page"""
@app.route("/")
def index():
    return render_template("index.html")
    
    

"""Rendering the signup page and dealing with the form"""
@app.route("/signup")
def signup():
    return render_template("signup.html")



"""Rendering the login page and dealing with the form"""
@app.route("/login")
def login():
    return render_template("login.html")
    
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)