from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

username = os.getenv('C9_USER')
app = Flask(__name__)
app.secret_key = "SECRET KEY"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://yubehjsptoqvok:b0c1593f028ea0af4c8d2b656f070b3a80e55b36c97831a847b9f6a507795644@ec2-54-75-230-41.eu-west-1.compute.amazonaws.com:5432/d340c3tp066fuc')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from therecipestore import routes