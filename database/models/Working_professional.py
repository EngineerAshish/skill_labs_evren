from datetime import datetime

from flask import jsonify


from ..db import db
from .Mentornship import Mentornship

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

    @classmethod
    def get_working_professionals(cls, page, email):

        per_page = 10
        mentors = Mentornship.get_mentornships_by_student_email(email)
        already_applied_id = []
        for x in mentors:
            already_applied_id.append(int(x["working_professional_id"]))

        working_professionals = cls.query.paginate(page,per_page,error_out=False).items
        working_professionals_list = [] 
        # working_professionals_json = {}
        # count = 1
        # for c in working_professionals:
        #     working_professionals_json[count] = c.json()
        #     count = count+1
        for w in working_professionals:

            if not int(w.json()["id"]) in already_applied_id: 
                working_professionals_list.append(w.json())

        return working_professionals_list

