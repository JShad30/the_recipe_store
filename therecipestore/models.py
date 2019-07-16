from datetime import datetime
from therecipestore import db, login_manager
from flask_login import UserMixin


"""Gets the sessions working for different users"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""Tables for the database being created with SQLAlchemy"""
#User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    username = db.Column(db.String(25), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    recipes = db.relationship('Recipe', backref="author", lazy=True)

    def __repr__(self):
        return 'User({0}, {1}, {2}, {3}, {4})'.format(self.firstname, self.lastname, self.username, self.email, self.password)
        
#Recipes table
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(20))
    recipe_description = db.Column(db.String(200))
    recipe_difficulty = db.Column(db.String(10))
    recipe_prep_time = db.Column(db.String(20))
    recipe_cook_time = db.Column(db.String(20))
    meal_type = db.Column(db.String(15))
    """preference = db.Column(db.String(25))
    allergen = db.Column(db.String(25))"""
    
    meal_preference_vegetarian = db.Column(db.Boolean)
    meal_preference_vegan = db.Column(db.Boolean)
    meal_preference_pescatarian = db.Column(db.Boolean)
    meal_preference_raw_vegetarian = db.Column(db.Boolean)

    meal_allergen_nut_free = db.Column(db.Boolean)
    meal_allergen_lactose_free = db.Column(db.Boolean)
    meal_allergen_gluten_free = db.Column(db.Boolean)

    recipe_added = db.Column(db.DateTime, default=datetime.utcnow)
    recipe_score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ingredients = db.relationship('Ingredient', backref="recipe", lazy=True)
    instructions = db.relationship('Instruction', backref="recipe", lazy=True)
    
    def __repr__(self):
        return 'Recipe({0}, {1}, {2}, {3}, {4}, {5})'.format(self.recipe_name, self.recipe_description, self.meal_type, self.recipe_added, self.ingredients, self.instructions)
        
#Ingredients table
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(30))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    
    def __repr__(self):
        return 'Ingredient({0})'.format(self.ingredient_name)

#Instructions table
class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instruction_name = db.Column(db.String(200))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    
    def __repr__(self):
        return 'Instructions({0})'.format(self.instruction_name)
