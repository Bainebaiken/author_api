from authors_app import db
from datetime import datetime

class Company(db.Model):
    __tablename__ = "companies"  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))  
    user = db.relationship('User', backref='companies')  # Define the relationship with User model
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    # Constructor
    def __init__(self, name, description, user_id):  
        self.name = name
        self.description = description
        self.user_id = user_id








# from authors_app import db
# from datetime import datetime

# class company(db.Model):
#  __table__="company"
#  id =db.Column(db.Integer,primay_key=True)
#  name=db.Column(db.String(50),nullable=False,unique=True)
#  description=db.Column(db.String(100),nullable=False)
#  user_id =db.Column(db.Integer, db.foreign_key("users"))
#  #user=db.relationship('User',backref='companies')
#  created_at=db.Column(db.DateTime,default=datetime.now())
#  updated_at=db.Column(db.DateTime,onupdate=datetime.now())   

# def __init__(self,name,description,origin):
#     self.name=name
#     self.description=description
#     self.origin=origin


#     def __init__(self):
#         return f"<company(name='{self.name}',origin='{self.origin}')"