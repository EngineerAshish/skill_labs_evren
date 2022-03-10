from datetime import datetime
from ..db import db

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MSME_id = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    number_of_interns = db.Column(db.Integer)
    MSME_name = db.Column(db.String(100), unique=True)
    stipend = db.Column(db.DECIMAL(19, 4))
    requirements = db.Column(db.String(100))
    time_period = db.Column(db.DECIMAL(19, 4))
    status = db.Column(db.Integer)
    perks = db.Column(db.String(100))
    position = db.Column(db.String(100))
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


    def save_profile(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_profile_by_email(cls,email):
        return cls.query.filter_by(email=email).first()


    @classmethod
    def get_profile_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def delete_profile(cls,id):
        cls.query.filter_by(id=id).delete()
        db.session.commit()

    @classmethod
    def get_profile_status(cls,email):
        current_user = cls.get_profile_by_email(email)
        current_user_json = current_user.json()
        return current_user_json["profile_completed"]
