from flask_sqlalchemy import SQLAlchemy

# create a new SQLAlchemy object
db = SQLAlchemy()


# Base model that for other models to inherit from
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())

class Admin(Base):

    # Columns declaration
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255),unique=True)
    phone = db.Column(db.String(255),unique=True) 
    def __repr__(self):
        # a user friendly way to view our objects in the terminal
        return self.name
 def __repr__(self):
        # a user friendly way to view our objects in the terminal
        return self.name

class ScannedImages(Base):
    img = db.Column(db.String,)
    output =  db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
    

# class Media(Base):
#     pass
