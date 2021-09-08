from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d0b6dad9e09995ed085ffacff2f7173'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# this import causes routes.py to run which addes the routes to the app
from flaskblog import routes