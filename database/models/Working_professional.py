from datetime import datetime
from ..db import db


class Working_professional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    designation = db.Column(db.String(100))
    location = db.Column(db.String(100))
    organisation = db.Column(db.String(100))
    user_id = db.Column(db.Integer) 
    email = db.Column(db.String(100), unique=True)
    UG_degree = db.Column(db.String(100))
    PG_degree = db.Column(db.String(100))
    current_company = db.Column(db.String(100))
    intrested_area = db.Column(db.String(100))
    working_experience = db.Column(db.Integer)
    created_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
    updated_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False,onupdate=datetime.utcnow())
    


    def json(self):
        self_dict = self.__dict__
        user_dict = {x:self_dict[x] for x in self_dict.keys() if not x.startswith("_") and x!="enc_password"}
        return (user_dict)


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_by_email(cls,email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_user_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def delete_user(cls,id):
        cls.query.filter_by(id=id).delete()
        db.session.commit()