from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '3d0b6dad9e09995ed085ffacff2f7173'


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
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)