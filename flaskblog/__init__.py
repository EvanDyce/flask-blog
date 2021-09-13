from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d0b6dad9e09995ed085ffacff2f7173'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
# funciton name of login route
# used for login required things
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# this import causes routes.py to run which addes the routes to the app
from flaskblog import routes