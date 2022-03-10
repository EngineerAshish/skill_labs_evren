from datetime import datetime
from enum import unique

from sqlalchemy import true
from ..db import db

class MSME(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    type = db.Column(db.Integer, nullable=False)
    business_category = db.Column(db.String(100))
    business_type= db.Column(db.String(100))
    business_name= db.Column(db.String(100))
    firm_type= db.Column(db.String(100))
    gst_number= db.Column(db.String(100))
    urn_number= db.Column(db.String(100))
    date_of_incorporation= db.Column(db.DateTime)
    functional_areas= db.Column(db.String(100))
    upload_docs= db.Column(db.String(100))
    intrested_areas= db.Column(db.String(100))
    location = db.Column(db.String(100))
    turnover = db.Column(db.String(100))
    created_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
    updated_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False,onupdate=datetime.utcnow())
    

    def json(self):
        self_dict = self.__dict__
        user_dict = {}
        total_keys = 0
        total_set_keys = 0
        for x in self_dict.keys():
            if not x.startswith("_") and x!="enc_password":
                user_dict[x] = self_dict[x]
                total_keys+=1
                # check if the key is set
                if self_dict[x]:
                    total_set_keys +=1
        total_set_keys = total_set_keys/total_keys *100
        user_dict["profile_completed"] = total_set_keys
        # user_dict = {x:self_dict[x] for x in self_dict.keys() if not x.startswith("_") and x!="enc_password"}
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

    @classmethod
    def get_profile_status(cls,email):
        current_user = cls.get_user_by_email(email)
        current_user_json = current_user.json()
        return current_user_json["profile_completed"]