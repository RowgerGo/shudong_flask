# coding: utf-8
from sqlalchemy import Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy

from application import db
# db = SQLAlchemy()


class YiAdmin(db.Model):
    __tablename__ = 'yi_admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    login_salt = db.Column(db.String(50), nullable=True)
    lastip = db.Column(db.Integer, nullable=False)
    lasttime = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Text, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    admin = db.Column(db.Integer, nullable=False)
