import json
from flask import render_template, request, flash, redirect, url_for
from therecipestore import app, db, bcrypt
from therecipestore.forms import Signup, Login, UpdatePersonalHome, CreateRecipe, RateRecipe
from therecipestore.models import User, Recipe, Ingredient, Instruction
from flask_login import login_user, current_user, logout_user, login_required



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
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Welcome to theRecipeStore. You can now log in')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)


"""Rendering the login page and dealing with the form"""
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
    	return redirect(url_for('personal_home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #Go to the next page if it exists. If it doesn't redirect to the home page
            nextpage = request.args.get('next')
            return redirect(nextpage) if nextpage else redirect(url_for('personal_home'))
        else:
            flash('Either the email or password are incorrect, please try again.')
    return render_template('login.html', title='Log In', form=form)


"""Execute when the user clicks the logout button"""    
@app.route("/logout")
def logout():
    logout_user()
    flash("You are now logged out. Thanks for using theRecipeStore, we hope to see you again soon!")
    return redirect(url_for("login"))

    

"""Rendering the personal pages"""
@app.route("/personal_home", methods=['GET', 'POST'])
@login_required
def personal_home():
    form = UpdatePersonalHome()
    if form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your personal details have now been updated")
        return redirect(url_for("personal_home"))
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template("userhome.html", title="Personal Page", form=form)
    


"""Rendering the page where a user will build a new recipe"""
@app.route("/create_recipe", methods=["GET", "POST"])
@login_required
def create_recipe():
    form = CreateRecipe()
    if form.validate_on_submit():
        recipe = Recipe(recipe_name=form.recipe_name.data, recipe_description=form.recipe_description.data, recipe_difficulty=form.recipe_difficulty.data, recipe_prep_time=form.recipe_prep_time.data, recipe_cook_time=form.recipe_cook_time.data, recipe_score=0, author=current_user)
        ingredient = Ingredient(ingredient_name=form.ingredient_name.data)
        instruction = Instruction(instruction_name=form.instruction_name.data)
        db.session.add(recipe)
        db.session.add(ingredient)
        db.session.add(instruction)
        db.session.commit()
        flash("Your recipe has been created")
        return redirect(url_for("personal_home"))
    return render_template("createrecipe.html", form=form)



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
    form = RateRecipe()
    return render_template("recipe.html", form=form)