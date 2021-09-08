from flask import render_template, url_for, redirect
from flask.helpers import flash

from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import Post, User

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

