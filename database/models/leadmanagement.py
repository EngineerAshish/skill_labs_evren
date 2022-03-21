from pymysql import NULL
from ..db import db

class leadmanagement(db.Model):
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    sub_category = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    service_name = db.Column(db.String(100))
    status = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)
    assigned_to = db.Column(db.String(100),default=NULL)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_lead_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    





class new(db.Model):
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    sub_category = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    service_name = db.Column(db.String(100))
    status = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)
    assigned_to = db.Column(db.String(100),default=NULL)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_lead_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    




class assigned(db.Model):
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    sub_category = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    service_name = db.Column(db.String(100))
    status = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)
    assigned_to = db.Column(db.String(100),default=NULL)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_lead_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    



class pending(db.Model):
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    sub_category = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    service_name = db.Column(db.String(100))
    status = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)
    assigned_to = db.Column(db.String(100),default=NULL)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_lead_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    



class converted(db.Model):
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    sub_category = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    service_name = db.Column(db.String(100))
    status = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)
    assigned_to = db.Column(db.String(100),default=NULL)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_lead_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    



class rejected(db.Model):
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    sub_category = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    service_name = db.Column(db.String(100))
    status = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)
    assigned_to = db.Column(db.String(100),default=NULL)
    
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_lead_by_id(cls,id):
        return cls.query.filter_by(id=id).first()