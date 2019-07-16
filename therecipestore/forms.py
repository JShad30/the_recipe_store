from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField, FileField, RadioField, SelectField, FieldList
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
                
                

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired(), Length(min=2, max=40)])
    recipe_description = TextAreaField('Recipe Description', validators=[DataRequired()])
    recipe_difficulty = SelectField('Difficulty Level', choices=[('easy', 'Easy'),('medium', 'Medium'),('difficult', 'Difficult')], validators=[DataRequired()])
    recipe_prep_time = StringField('Preparation Time', validators=[DataRequired()])
    recipe_cook_time = StringField('Cooking Time', validators=[DataRequired()])
    meal_type = RadioField('Meal Type', choices=[('light_bites','Light Bites'),('snacks','snacks'),('main_meals','Main Meals'),('desserts','desserts')], validators=[DataRequired()])
    """preference = RadioField('Preference', choices=[('vegetarian','Vegetarian'),('vegan','Vegan'),('pescatarian','Pescatarian'),('raw_vegetarian','Raw Vegetarian')])
    allergen = RadioField('Allergen', choices=[('lactose_free','Lactose Free'),('nut_free','Nut Free'),('gluten_free','Gluten Free')])"""
    meal_preference_vegetarian = BooleanField('Vegetarian')
    meal_preference_vegan = BooleanField('Vegan')
    meal_preference_pescatarian = BooleanField('Pescatarian')
    meal_preference_raw_vegetarian = BooleanField('Raw Vegetarian')

    meal_allergen_nut_free = BooleanField('Nut Free')
    meal_allergen_lactose_free = BooleanField('Lactose Free')
    meal_allergen_gluten_free = BooleanField('Gluten Free')
    
    ingredients = FieldList(StringField('Recipe Ingredient'), min_entries=3, max_entries=15)
    instructions = FieldList(TextAreaField('Recipe Instruction'), min_entries=3, max_entries=15)
    
    submit = SubmitField('Create Recipe')