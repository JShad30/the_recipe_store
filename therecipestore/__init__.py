from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

username = os.getenv('C9_USER')
app = Flask(__name__)
app.secret_key = "SECRET KEY"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///the_recipe_store.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from therecipestore import routes