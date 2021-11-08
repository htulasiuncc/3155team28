import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

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

