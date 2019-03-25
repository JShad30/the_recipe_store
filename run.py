import os
import json
from flask import Flask, render_template

app = Flask(__name__)

"""Rendering the home page"""
@app.route("/")
def index():
    data = []
    with open("static/data/meal-type-homepage.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", meal_type_statements=data)
    
    

"""Rendering the signup page and dealing with the form"""
@app.route("/signup")
def signup():
    return render_template("signup.html")



"""Rendering the login page and dealing with the form"""
@app.route("/login")
def login():
    return render_template("login.html")
    
    
    
"""Rendering the contact page with form"""
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
    
    
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