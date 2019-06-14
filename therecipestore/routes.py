import json
from flask import Flask, render_template, request, flash, redirect, url_for
from therecipestore import app, db, bcrypt
from therecipestore.forms import Signup, Login
from therecipestore.models import User
from flask_login import login_user, current_user



"""Routes"""
"""Rendering the home page"""
@app.route("/")
@app.route("/home")
def index():
    data = []
    with open("therecipestore/static/data/meal-type-homepage.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", meal_type_statements=data)
    
    
    
@app.route("/<meal_type>")
def meal_type_page(meal_type):
    mealtype = {}
    
    with open("therecipestore/static/data/meal-type-homepage.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == meal_type:
                mealtype = obj
        
    return render_template("mealtype.html", mealtype=mealtype)
    
    
        
"""Rendering the about page with form"""
@app.route("/about")
def about():
    return render_template("about.html")
    
    

"""Rendering the signup page and dealing with the form"""
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
    	return redirect(url_for('index'))
    form = Signup()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    	user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data, password=form.password.data)
    	db.session.add(user)
    	db.session.commit()
    	flash('Welcome to theRecipeStore. You can now log in')
    	return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)


"""Rendering the login page and dealing with the form"""
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Either the email or password are incorrect, please try again.')
    return render_template('login.html', title='Log In', form=form)
    
    
    
    

"""Execute when the user clicks the logout button"""    
@app.route("/logout")
def logout():
    flash("You are now logged out. Thanks for using theRecipeStore, we hope to see you again soon!")
    return redirect(url_for("login"))

    

"""Rendering the personal pages"""
@app.route("/personal_home/<username>")
def personal_home(username):
    print('{}'.format(username))
    return render_template("userhome.html", firstname='', lastname='', username=username, email='', password='')
    


"""Rendering the contact page with form"""
@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")
    
    
    
"""Page to be redirected to when message received"""  
@app.route("/message_received")
def message_received():
    return render_template("messagereceived.html")
    
    
    
"""Rendering the Meal types Pages"""
@app.route("/meal_type")
def meal_type():
    return render_template("mealtype.html")
    
    
    
"""Rendering the Allergen Pages"""
@app.route("/preference")
def preference():
    return render_template("mealtype.html")



"""Rendering the Allergen Pages"""
@app.route("/allergen")
def allergen():
    return render_template("mealtype.html")
    
    
    
"""Rendering each of the individual recipe pages"""
@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    return render_template("recipe.html")
    


"""Rendering the page where a user will build a new recipe"""
@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    return render_template("createrecipe.html")