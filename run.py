import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mail import Mail, Message
from datetime import datetime
import pymysql

username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='theRecipeStore')

app = Flask(__name__)
app.secret_key = "secret_message"


"""Rendering the home page"""
@app.route("/")
@app.route("/home")
def index():
    data = []
    with open("static/data/meal-type-homepage.json", "r") as json_data:
        data = json.load(json_data)
        
    #with connection.cursor() as cursor:
        #Search through the database where 
        #cursor.execute("SELECT * FROM Recipes ORDER BY SCORE WHERE TimeCreated='%s'", )
        #cursor.execute("SELECT * FROM Recipes ORDER BY SCORE WHERE Allergen='%s'", )
        
    return render_template("index.html", meal_type_statements=data)
    
    
    
@app.route("/<meal_type>")
def meal_type_page(meal_type):
    mealtype = {}
    
    with open("static/data/meal-type-homepage.json", "r") as json_data:
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
    session.clear()
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        with connection.cursor() as cursor:
            row = (firstname, lastname, username, email, password)
            cursor.execute("INSERT INTO user (firstname, lastname, username, email, password) VALUES (%s, %s, %s, %s, %s)", row)
            connection.commit()
            flash("Hi {0}. Many thanks for registering. You can now login".format(request.form["firstname"]))
        return redirect(url_for("login", username=username, firstname=firstname))
    return render_template("signup.html")



"""Rendering the login page and dealing with the form"""
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usernamelogin = request.form["username"]
        passwordlogin = request.form["password"]
        with connection.cursor() as cursor:
            result = cursor.execute("SELECT firstname, lastname, username, email, password FROM user WHERE username = %s", (usernamelogin,))
            print(result)
            firstname, lastname, username, email, password = cursor.fetchone()
            print(username)
            print(password)
            if username is None:
                flash("Incorrect login details, try again")
                return render_template("login.html")
            else:
                if password == passwordlogin:
                    session["log"] = True
                    flash("Hi {0}, welcome to your theRecipeStore account".format(request.form["username"]))
                    return redirect(url_for("personal_home", username=username))
                else:
                    flash("Incorrect login details, try again")
                    return render_template("login.html")
    return render_template("login.html")
    
    

"""Execute when the user clicks the logout button"""    
@app.route("/logout")
def logout():
    session.clear()
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
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        flash("Thank you for your message {0} {1}. We have received your message and somebody will get back to you at {2}".format(request.form["firstname"], request.form["lastname"], request.form["email"]))
        return redirect(url_for("message_recieved"))
    return render_template("contact.html")
    
    
    
"""Page to be redirected to when message received"""  
@app.route("/message_received")
def message_received(firstname, lastname, email, message):
    return render_template("messagereceived.html", firstname=firstname, lastname=lastname, email=email)
    
    
    
"""Rendering the Meal types Pages"""
@app.route("/meal_type")
def meal_type():
    with connection.cursor() as cursor:
        #Search through the database where 
        cursor.execute("SELECT * FROM Recipes ORDER BY SCORE WHERE MealType='%s'", )
    return render_template("mealtype.html")
    
    
    
"""Rendering the Allergen Pages"""
@app.route("/preference")
def preference():
    with connection.cursor() as cursor:
        #Search through the database where 
        cursor.execute("SELECT * FROM Recipes ORDER BY SCORE WHERE Preference='%s'", )
    return render_template("mealtype.html")



"""Rendering the Allergen Pages"""
@app.route("/allergen")
def allergen():
    with connection.cursor() as cursor:
        #Search through the database where 
        cursor.execute("SELECT * FROM Recipes ORDER BY SCORE WHERE Allergen='%s'", )
    return render_template("mealtype.html")
    
    
    
"""Rendering each of the individual recipe pages"""
@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    return render_template("recipe.html")
    


"""Rendering the page where a user will build a new recipe"""
@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    if request.method == "POST":
        
        """Setting the variables from the created recipe form"""
        
        #Recipe name and description
        recipe_name = request.form["recipe-name"]
        recipe_description = request.form["recipe-description"]
        
        #Recipe cooking information
        difficulty_level = request.form["difficulty-level"]
        preparation_time = request.form["preparation-time"]
        cooking_time = request.form["cooking-time"]
        
        #Recipe Meal Type takes info from selection of radio button section
        choice_mealtype = request.form["choice-mealtype"]
        
        #Check whether checkboxes are checked - if yes then add 'Y', if no then add 'N'
        choice_preference = request.form[""]
        choice_allergen = request.form[""]
        
        #Recipe ingrediets section
        ingredientname = request.form[""]
        
        #Recipe instructions section
        instruction = request.form[""]
        
        """Inserting those variables into the database"""
        with connection.cursor() as cursor:
            #Inserting into the recipes table
            row = (recipe_name, recipe_description, difficulty_level, preparation_time, cooking_time)
            recipe_name_add = cursor.execute("INSERT INTO Recipe (recipename, recipedescription, allergyid, preferenceid, mealtypeid, createdby, timecreated, score", row).fetchone()
            
            #Inserting into the ingredients table
            ingredients_add = cursor.execute("INSERT INTO Ingredients (ingredientname) VALUES ('%s')", ingredientname)
            
            #Inserting into the instructions table
            instructions_add = cursor.execute("INSERT INTO Ingredients (instruction) VALUES ('%s')", instruction)
        
        return redirect(url_for("personal_home"))
    return render_template("createrecipe.html")
    
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)