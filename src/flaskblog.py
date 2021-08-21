from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/test")
def temp():
    return render_template("test.html", title="Test")

if __name__ == '__main__':
    app.run(debug=True)