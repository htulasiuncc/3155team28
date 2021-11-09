import os
from flask import Flask
from flask import render_template
from database import db
from models import Post as Post
from models import User as User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()  # run under the app context


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def aboutUs():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/addPost')
def addPost():
    return render_template('addPost.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signUp')
def sign_up():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
