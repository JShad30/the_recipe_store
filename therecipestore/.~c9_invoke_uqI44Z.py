from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField, FileField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from therecipestore.models import User, Recipe, Ingredient, Instruction



class Signup(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    """Check whether the username has been used before, if it has return an error to tell the user they must choose a different username"""
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('An account with that username already exists, please try another.')

    """Check whether the email has been used before, if it has return an error to ask the user whether they already have an account"""
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken by a member. Do you already have an account?')


    
class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')



class UpdatePersonalHome(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update Details')
    
    """Ensure that the username has not been taken by another user previously, unless it is the current, logged in user"""
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('An account with that username already exists, please try another.')
                
    """Ensure that the email has not been taken by another user previously, unless it is the current, logged in user"""
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already taken by a member. Do you already have an account?')
                
                

class CreateRecipe(FlaskForm):
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    recipe_name = StringField('Recipe Name', validators=[DataRequired(), Length(min=2, max=40)])
    recipe_description = TextAreaField('Recipe Description', validators=[DataRequired()])
    recipe_difficulty = SelectField('Difficulty Level', choices=[('value_one','Easy'),('value_two','Medium'),('value_three','Difficult')], validators=[DataRequired()])
    recipe_prep_time = StringField('Preparation Time', validators=[DataRequired()])
    recipe_cook_time = StringField('Cooking Time', validators=[DataRequired()])
    meal_type = RadioField('Meal Type', choices=[('value_one','Light Bites'),('value_two','Snacks'),('value_three','Main Meals'),('value_four','Desserts')])
    
    meal_preference_vegetarian = BooleanField('Meal Type', choices=[('value_one','Vegetarian'),('value_two','Pescatarian'),('value_three','Vegan'),('value_four','Raw Vegetarian')])
    meal_preference_vegetarian
    meal_preference_Pescatarian
    meal_preference_
    
    meal_allergen = BooleanField('Meal Type', choices=[('value_one','Nut Free'),('value_two','Lactose Free'),('value_three','Gluten Free')])
    recipe_ingredient = StringField('Recipe Ingredient')
    recipe_instruction = TextAreaField('Recipe Ingredient')
    submit = SubmitField('Create Recipe')
    

#The following is for the like button on the recipe pages. This will add one to the recipe score when pressed.
class RateRecipe(FlaskForm):
    submit = SubmitField('Score Recipe')