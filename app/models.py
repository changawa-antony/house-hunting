from . import db
from flask_login import UserMixin

class bookAppointment(UserMixin, db.Model):
    """User booking model."""

    __tablename__ = 'booking'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )

    phone = db.Column(
        db.Integer(100),
        nullable=False,
        unique=False
    )

    email = db.Column(
        db.String(40),
        nullable=False,
        unique=False
    )

class posts(UserMixin, db.Model):
    """User booking model."""
    
    __tablename__ = 'posts'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )

    description = db.Column(
        db.Integer(100),
        nullable=False,
        unique=False
    )

    photo = db.Column(
        db.LargeBinary(40),
        nullable=False,
        unique=False
    )