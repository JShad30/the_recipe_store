import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_message"

"""Rendering the home page"""
@app.route("/")
def index():
    data = []
    with open("static/data/meal-type-homepage.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", meal_type_statements=data)
    
    

"""Rendering the signup page and dealing with the form"""
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        session["username"] = username
        session["firstname"] = firstname
        session["lastname"] = lastname
        flash("{0}, Welcome to theRecipeStore".format(request.form["firstname"]))
        return redirect(url_for("personal_home", username=session["username"]))
    return render_template("signup.html")
    
    
    
"""Rendering the personal pages"""
@app.route("/<username>")
def personal_home(username):
    return render_template("userhome.html", username=session["username"])



"""Rendering the login page and dealing with the form"""
@app.route("/login")
def login():
    return render_template("login.html")
    
    
    
    
    
    
"""The following is the page to redirect to when the contact form is filled in - speak to mentor regarding the contact redirects"""    
    
"""Rendering the contact page with form"""
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        flash("Thank you for your message {0} {1}. We have received your message and somebody will get back to you at {2}".format(request.form["firstname"], request.form["lastname"], request.form["email"]))
        return redirect(url_for("messagereceived.html", firstname=firstname, lastname=lastname, email=email))
    return render_template("contact.html")
    
    
    
"""Page to be redirected to when message received"""  
@app.route("/message_received")
def message_received(firstname, lastname, email):
    return render_template("messagereceived.html", firstname=firstname, lastname=lastname, email=email)
    
    
    
    
    
"""Rendering the about page with form"""
@app.route("/about")
def about():
    return render_template("about.html")
    
    
    
"""Rendering the Meal types Pages"""
@app.route("/meal_type")
def meal_type():
    return render_template("mealtype.html")



"""Rendering the Allergen Pages"""
@app.route("/allergen")
def allergen():
    return render_template("allergen.html")



"""Rnedering the most popular and the most recently added recipes""" 
    
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)