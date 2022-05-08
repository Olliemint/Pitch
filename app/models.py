from datetime import date
from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username =db.Column(db.String(15),unique=True, nullable=False)
    email =db.Column(db.String(100),unique=True, nullable=False)
    avatar =db.Column(db.String(60), nullable=False, default ='default.jpg')
    password =db.Column(db.String(60), nullable=False)
    pitchs = db.relationship('Pitch',backref = 'author', lazy =True)
    def __repr__(self):
        
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Pitch(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(100), nullable=False)
    posted = db.Column(db.DateTime,nullable = False, default = date.ctime)
    pitch = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    
    
    
    def __repr__(self):
        
        return f"Pitch('{self.title}','{self.posted}')"
    