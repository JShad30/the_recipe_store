import json
from flask import render_template, request, flash, redirect, url_for, abort
from therecipestore import app, db, bcrypt
from therecipestore.forms import Signup, Login, UpdatePersonalHome, RecipeForm
from therecipestore.models import User, Recipe, Ingredient, Instruction
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import true, false
from sqlalchemy.orm import lazyload



"""Routes"""
"""Rendering the home page"""
@app.route("/")
@app.route("/home")
def index():
    recipes_dated = Recipe.query.order_by(Recipe.recipe_added.desc())[:12]
    data = []
    with open("therecipestore/static/data/meal-type-homepage.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", meal_type_statements=data, recipes_dated=recipes_dated)



"""Function to download the data from the json file to be used in the meal_type, preference and allergen routes"""
def load_data(meal_type):
    mealtype = {}
    with open("therecipestore/static/data/meal-type-homepage.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == meal_type:
                mealtype = obj
    return mealtype                

"""Specific meal type pages to show recipes on chosen meal type"""    
@app.route("/meal_type/<meal_type>")
def meal_type_page(meal_type):
    mealtype = load_data(meal_type)
    recipes = Recipe.query.filter_by(meal_type=meal_type).order_by(Recipe.recipe_added.desc())

    return render_template("mealtype.html", mealtype=mealtype, recipes=recipes)
    
"""Specific preference pages to show recipes on chosen preference"""    
@app.route("/preference/<meal_type>")
def preference(meal_type):
    mealtype = load_data(meal_type)
    if meal_type == 'vegetarian':
        recipes = Recipe.query.filter_by(meal_preference_vegetarian=true()).order_by(Recipe.recipe_added.desc())
    if meal_type == 'vegan':
        recipes = Recipe.query.filter_by(meal_preference_vegan=true()).order_by(Recipe.recipe_added.desc())
    if meal_type == 'pescatarian':
        recipes = Recipe.query.filter_by(meal_preference_pescatarian=true()).order_by(Recipe.recipe_added.desc())
    if meal_type == 'raw_vegetarian':
        recipes = Recipe.query.filter_by(meal_preference_raw_vegetarian=true()).order_by(Recipe.recipe_added.desc())

    return render_template("mealtype.html", mealtype=mealtype, recipes=recipes)
    
"""Specific allerge pages to show recipes on chosen allergen"""    
@app.route("/allergen/<meal_type>")
def allergen(meal_type):
    mealtype = load_data(meal_type)
    if meal_type == 'nut_free':
        recipes = Recipe.query.filter_by(meal_allergen_nut_free=true()).order_by(Recipe.recipe_added.desc())
    if meal_type == 'lactose_free':
        recipes = Recipe.query.filter_by(meal_allergen_lactose_free=true()).order_by(Recipe.recipe_added.desc())
    if meal_type == 'gluten_free':
        recipes = Recipe.query.filter_by(meal_allergen_gluten_free=true()).order_by(Recipe.recipe_added.desc())
        
    return render_template("mealtype.html", mealtype=mealtype, recipes=recipes)

    
    
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
    recipes = Recipe.query.order_by(Recipe.recipe_added.desc())
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
    return render_template("userhome.html", title="Personal Page", form=form, recipes=recipes)
    

    
"""Rendering the page where a user will build a new recipe"""
@app.route("/create_recipe", methods=["GET", "POST"])
@login_required
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            recipe_name=form.recipe_name.data,
            recipe_description=form.recipe_description.data,
            recipe_difficulty=form.recipe_difficulty.data,
            recipe_prep_time=form.recipe_prep_time.data,
            recipe_cook_time=form.recipe_cook_time.data,
            meal_type=form.meal_type.data,
            meal_preference_vegetarian=form.meal_preference_vegetarian.data,
            meal_preference_vegan=form.meal_preference_vegan.data,
            meal_preference_pescatarian=form.meal_preference_pescatarian.data,
            meal_preference_raw_vegetarian=form.meal_preference_raw_vegetarian.data,
            meal_allergen_nut_free=form.meal_allergen_nut_free.data,
            meal_allergen_lactose_free=form.meal_allergen_lactose_free.data,
            meal_allergen_gluten_free=form.meal_allergen_gluten_free.data,
            author=current_user,
            ingredients=[],
            instructions=[])
        for ingredient in form.ingredients.data:
            recipe.ingredients.append(Ingredient(ingredient_name=ingredient))
        for instruction in form.instructions.data:
            recipe.instructions.append(Instruction(instruction_name=instruction))
        db.session.add(recipe)
        db.session.commit()
        flash("Your recipe has been created")
        return redirect(url_for("personal_home"))
    return render_template("createrecipe.html", form=form, legend='Create Recipe')
    
    

"""Rendering each of the individual recipe pages"""
@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
    recipe = Recipe.query.filter_by(id=id).options(lazyload(Recipe.ingredients)).first()
    print(recipe)
    return render_template('recipe.html', title=recipe.recipe_name, recipe=recipe)
    
    
    
"""Updating a recipe. Only available to the user who uploaded the recipe"""
@app.route("/recipe/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    # Print an error if the user trying to access the update page is not the owner of that recipe
    if recipe.author != current_user:
        abort(403)
    form = RecipeForm()
    if form.validate_on_submit():
        recipe.recipe_name = form.recipe_name.data
        recipe.recipe_description = form.recipe_description.data
        recipe.recipe_difficulty = form.recipe_difficulty.data
        recipe.recipe_prep_time = form.recipe_prep_time.data
        recipe.recipe_cook_time = form.recipe_cook_time.data
        recipe.meal_type = form.meal_type.data
        recipe.meal_preference_vegetarian = form.meal_preference_vegetarian.data
        recipe.meal_preference_vegan = form.meal_preference_vegan.data
        recipe.meal_preference_pescatarian = form.meal_preference_pescatarian.data
        recipe.meal_preference_raw_vegetarian = form.meal_preference_raw_vegetarian.data
        recipe.meal_allergen_nut_free = form.meal_allergen_nut_free.data
        recipe.meal_allergen_lactose_free = form.meal_allergen_lactose_free.data
        recipe.meal_allergen_gluten_free = form.meal_allergen_gluten_free.data
        """for ingredient in form.ingredients.data:
            recipe.ingredients = form.ingredients.data
        for instruction in form.instructions.data:
            recipe.instructions = form.instruction.data"""
        db.session.commit()
        flash('Your recipe has been updated')
        return redirect(url_for('recipe', id=recipe.id))
    elif request.method == 'GET':
        form.recipe_name.data = recipe.recipe_name
        form.recipe_description.data = recipe.recipe_description
        form.recipe_difficulty.data = recipe.recipe_difficulty
        form.recipe_prep_time.data = recipe.recipe_prep_time
        form.recipe_cook_time.data = recipe.recipe_cook_time
        form.meal_type.data = recipe.meal_type
        form.meal_preference_vegetarian.data = recipe.meal_preference_vegetarian
        form.meal_preference_vegan.data = recipe.meal_preference_vegan
        form.meal_preference_pescatarian.data = recipe.meal_preference_pescatarian
        form.meal_preference_raw_vegetarian.data = recipe.meal_preference_raw_vegetarian
        form.meal_allergen_nut_free.data = recipe.meal_allergen_nut_free
        form.meal_allergen_lactose_free.data = recipe.meal_allergen_lactose_free
        form.meal_allergen_gluten_free.data = recipe.meal_allergen_gluten_free
        """for ingredient in form.ingredients.data:
            form.ingredients.data = recipe.ingredients
        for instruction in form.instructions.data:
            form.instructions.data = recipe.instructions"""
    return render_template('createrecipe.html', form=form, legend='Update Recipe')
    
    
"""Delete button - when the user clicks this button the recipe is deleted from the database"""   
@app.route("/recipe/<int:id>/delete", methods=['POST'])
@login_required
def delete_recipe(id):
	recipe = Recipe.query.get_or_404(id)
	if recipe.author != current_user:
		abort(403)
	db.session.delete(recipe)
	db.session.commit()
	flash('Your recipe has been deleted')
	return redirect(url_for('personal_home'))



"""Rendering the contact page with form"""
@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")