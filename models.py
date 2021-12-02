from database import db
import datetime


class Post(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(100))
    img = db.Column("img", db.String(500))
    date = db.Column("date", db.String(50))
    view_count = db.Column(db.Integer, primary_key=False)
    report_count = db.Column(db.Integer, primary_key=False)
    # can create a foreign key: referencing the id variable in the User class,
    # so that is why it is lowerase u
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    comments = db.relationship("Comment", backref="post", cascade="all, delete-orphan", lazy=True)
    reports = db.relationship("Report", backref="post", cascade="all, delete-orphan", lazy=True)

    def __init__(self, title, text, img, date, view_count, report_count, user_id):
        self.title = title
        self.text = text
        self.img = img
        self.date = date
        self.view_count = view_count
        self.report_count = report_count
        self.user_id = user_id



class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    posts = db.relationship("Post", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.VARCHAR, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, content, post_id, user_id):
        self.date_posted = datetime.date.today()
        self.content = content
        self.post_id = post_id
        self.user_id = user_id


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue = db.Column(db.VARCHAR, nullable=False)
    content = db.Column(db.VARCHAR, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, issue, content, post_id, user_id):
        self.issue = issue
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
