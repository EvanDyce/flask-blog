from flask import render_template, url_for, redirect, request
from flask.helpers import flash
from flask_login import login_user, current_user, logout_user
from flask_login.utils import login_required

from flaskblog import app, db, bcrypt
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # makes form from forms.py
    form = RegistrationForm()

    # if it validates when posted flash message and return to home
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Your account has been created. You are now able to login', category='success')
        return redirect(url_for('login'))
    
    # if not re render the register.html file
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # if user is logged in redirects them straight to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # gets LoginForm
    form = LoginForm()

    # if it validates it chcks emails and flashes success and loads redirect
    # else flashes fail and reloads the login.html page
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Failed', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')