from datetime import datetime
from ..db import db

class Mentornship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100))
    working_professional_id = db.Column(db.String(100))
    student_name = db.Column(db.String(100))
    student_email = db.Column(db.String(100))
    mentor_name = db.Column(db.String(100))
    mentor_email = db.Column(db.String(100))
    status = db.Column(db.Integer)
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
        if total_keys == 0:
            total_keys = 1
            total_set_keys =1
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
    def get_mentornships_by_mentor_email(cls,email):
        mentornships_objs = cls.query.filter_by(mentor_email=email).all()
        mentornships = []

        for w in mentornships_objs:
            mentornships.append(w.json())
        
        return mentornships


    @classmethod
    def get_mentornships_by_student_email(cls,email):
        mentornships_objs = cls.query.filter_by(student_email=email).all()
        mentornships = []

        for w in mentornships_objs:
            mentornships.append(w.json())
        
        return mentornships


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
