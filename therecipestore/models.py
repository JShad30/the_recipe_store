from datetime import datetime
from therecipestore import db, app, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""Tables for the database being created with SQLAlchemy"""
#User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    recipes = db.relationship('Recipe', backref="author", lazy=True)

    def __repr__(self):
        return 'User({0}, {1}, {2}, {3}, {4})'.format(self.firstname, self.lastname, self.username, self.email, self.password)
        
#Recipe table
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(20), nullable=False)
    recipe_intro = db.Column(db.String(50), nullable=False)
    recipe_description = db.Column(db.String(200), nullable=False)
    recipe_image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    recipe_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    recipe_score = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return 'User({0}, {1}, {2}, {3}, {4}, {5})'.format(self.recipe_name, self.recipe_intro, self.recipe_description, self.recipe_image_file, self.recipe_added, self.recipe_score)