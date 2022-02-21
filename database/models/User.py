from datetime import datetime
from db import db


class User:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_nmber = db.Column(db.String(100), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)
    profile_image = db.Column(db.String(100), nullable=False)
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