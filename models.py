from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


#------------------------------------------------------------------------------
#user

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=True)
    phone = db.Column(db.String)
    imgurl = db.Column(db.String, nullable=True)
    role = db.Column(db.String(50), default='user')

    def __init__(self, id, name, email, password, phone, imgurl):
        self.id = id
        if (password):
            self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.imgurl = imgurl

    #relation-------

    appointments = db.relationship('Appointment', backref='user', lazy=True)
    Comment = db.relationship('Comment', backref='user', lazy=True)
    
    #----------------

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "imgurl": self.imgurl,
        }


#-----------------------------------------------------------------------------------
#avocat

class Avocat(User):


    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    Domaine = db.Column(db.string(50), default='avocat')
    cost = db.Column(db.string(50))
    website = db.Column(db.string)
    experience = db.Column(db.int)
    langue = db.Column(db.string(10) , default='fr')
    location = db.Column(db.string)

    #relation--------

    appointments = db.relationship('Appointment', backref='avocat', lazy=True)
    Comment = db.relationship('Comment', backref='avocat', lazy=True)
    
    #----------------

    def __init__(self, id, name, email, password, phone, imgurl):
        self.id = id
        if (password):
            self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.imgurl = imgurl
        self.role = 'Avocat'
        self.Domaine = Domaine
        self.cost = cost
        self.website = website
        self.experience = experience
        self.langue = langue
        self.location = location
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "imgurl": self.imgurl,
            "role": self.role,
            "Domaine": self.Domaine,
        }

#--------------------------------------------------------------------------------
#admin
class admin(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


#--------------------------------------------------------------------------------
#rendvu

class appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.String, primary_key=True)
    #relation user and avocat
    user_id = db.Column(db.string, db.ForeignKey('user.id'), nullable=False)
    avocat_id = db.Column(db.string, db.ForeignKey('avocat.id'), nullable=False)
    
    appointment_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    statue = db.Column(db.string, default='waiting')
    purpose = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Appointment {self.id} - {self.appointment_date}>"


#----------------------------------------------------------------------------------
#Comment

class Comment(db.Model):
    id = Column(db.string , primary_key=True)
    
    #relation user and avocat
    User_id = db.Column(db.string, db.ForeignKey('user.id'), nullable=False)
    avocat_id = db.Column(db.string, db.ForeignKey('avocat.id'), nullable=False)
    
    Comment_date = Column(db.DateTime, default=datetime.utcnow, nullable=False)
    content = db.Column(db.string)
    rating = db.Column(db.string)
