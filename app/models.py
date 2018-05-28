from app import create_app,db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    challenge_vid = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    group_relation = db.relationship("Groups", backref="user", lazy="dynamic")
    challenge_relation = db.relationship("Challenges", backref="user", lazy="dynamic")
    comment = db.relationship("Comments", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return 'User {}'.format(self.username)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    challenge_relation = db.relationship("Challenges", backref="category", lazy="dynamic")
    group_relation = db.relationship("Groups", backref="category", lazy="dynamic")


    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories

class Challenges(db.Model):
    all_pitches = []

    __tablename__ = 'challenges'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    challenge_vid = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    comment = db.relationship("Comments", backref="challenges", lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_challenges(cls):
        Challenges.all_challenges.clear()

    @classmethod
    def get_challenges(cls, id):
        challenges = Challenges.query.order_by(Challenges.date_posted.desc()).filter_by(category_id=id).all()
        return challenges

class Comments(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db. Integer, primary_key=True)
    comment_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.date_posted.desc()).filter_by(challenges_id=id).all()
        return comment

