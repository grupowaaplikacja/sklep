from flask_sqlalchemy import SQLAlchemy
from .. import application
from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    role = db.Column(db.Integer)

    def __reprt__(self):
        return '<User %r>' %self.email
    
    def __init__(self,email,password,first_name,last_name,phone,role=1):
        super(User,self).__init__(self,id,email,password,first_name,last_name,phone,role)

    db.create_all()



