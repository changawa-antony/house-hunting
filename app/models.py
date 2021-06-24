from . import db
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__='users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String())
    user_role = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    appointments = db.Column(db.Integer, db.ForeignKey('appointments.appointment_id'))
    posts_added = db.Column(db.Integer, db.ForeignKey('posts.post_id'))

    def verify_password(self, password):
        return (self.password, password)

    def get_id(self):
        return (self.user_id)


class Role(db.Model):
    __tablename__='roles'
    role_id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(100))
    user = db.relationship('User', backref='role', lazy='dynamic')

class Post(db.Model):
    __tablename__='posts'
    post_id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String(50))
    house_price = db.Column(db.String(255))
    house_location = db.Column(db.String(100))
    photo_path = db.Column(db.String())
    user = db.relationship('User', backref = 'posts', lazy='dynamic')
    category = db.Column(db.Integer, db.ForeignKey('categories.category_id'))

class Category(db.Model):
    __tablename__='categories'
    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    posts = db.relationship('Post', backref = 'posts', lazy='dynamic')

class Appointment(db.Model):
    __tablename__= 'appointments'
    appointment_id = db.Column(db.Integer, primary_key = True)
    appointment_title = db.Column(db.String(100))
    appointment_content = db.Column(db.String(255))
    appointment_date = db.Column(db.DateTime())
    appointment_made_on = db.Column(db.DateTime(), default = datetime.utcnow)
    user = db.relationship('User', backref='appointment', lazy='dynamic')