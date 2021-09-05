from flask import Flask, render_template, url_for, request
from flask.helpers import flash
from werkzeug.utils import redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '3d0b6dad9e09995ed085ffacff2f7173'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# class represents table in sql each one is a column
# this is user table 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # creates one to many relationship with Post column 
    # uses foreign key to get all posts made by the user
    # not a column, just a seperate query
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}'"



posts = [
    {
        'author' : 'Evan Dyce', 
        'title' : 'Blog Post 1', 
        'content' : 'First Post Content',
        'date_posted' : 'August 19, 2021'
    }, 
    {
        'author' : 'Josh Dyce', 
        'title' : 'Blog Post 2', 
        'content' : 'I am bad at golf',
        'date_posted' : 'August 19, 2021'
    }, 
    {
        'author' : 'Evan Dyce', 
        'title' : 'Flask', 
        'content' : 'I\'m making a flask thing',
        'date_posted' : 'August 19, 2021'
    }, 
    {
        'author' : 'Josh Dyce', 
        'title' : 'Blog Post 4', 
        'content' : 'I am so bad at golf and also suck at catan',
        'date_posted' : 'August 19, 2021'
    }
]

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    # makes form from forms.py
    form = RegistrationForm()

    # if it validates when posted flash message and return to home
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}', category='success')
        return redirect(url_for('home'))
    
    # if not re render the register.html file
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # gets LoginForm
    form = LoginForm()

    # if it validates it chcks emails and flashes success and loads redirect
    # else flashes fail and reloads the login.html page
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed', 'danger')

    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)