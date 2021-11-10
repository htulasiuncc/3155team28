import os
from flask import Flask
from flask import render_template
from database import db
from models import Post as Post
from models import User as User
from flask import redirect, url_for
from flask import request

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
    a_user = db.session.query(User).filter_by(email='xyz@uncc.edu').one()
    return render_template('index.html', user=a_user)


@app.route('/viewPosts')
def post():
    a_user = db.session.query(User).filter_by(email='xyz@uncc.edu').one()
    my_posts = db.session.query(Post).all()
    return render_template('viewPosts.html', posts=my_posts, user=a_user)


@app.route('/viewPosts/<post_id>')
def view_post(post_id):
    # retrieve user from database
    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu').one()
    # retrieve note from database
    my_post = db.session.query(Post).filter_by(id=post_id).one()
    return render_template('note.html', posts=my_post, user=a_user)


@app.route('/about')
def aboutUs():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/addPost', methods=['GET', 'POST'])
def addPost():
    if request.method == 'POST':
        # get title data
        title = request.form['title']
        # get note data
        text = request.form['content']
        # create data stamp
        name = request.form['createdBy']
        from datetime import date
        today = date.today()
        # format date mm/dd/yyyy
        today = today.strftime("%m-%d-%Y")
        new_record = Post(title, text, today)
        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for('post'))

    else:
        a_user = db.session.query(User).filter_by(email='xyz@uncc.edu').one()
        return render_template('addPost.html', user=a_user)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signUp')
def sign_up():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
