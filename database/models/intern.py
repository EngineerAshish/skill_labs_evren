from datetime import datetime
from ..db import db
# from .Internship import Internship

class Intern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    internship_id = db.Column(db.String(100))
    internship_email = db.Column(db.String(100))
    internship_name = db.Column(db.String(100))
    internship_company_name = db.Column(db.String(100))
    valid_till = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    student_id = db.Column(db.String(100))
    student_email = db.Column(db.String(100))
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
    def get_count_by_MSME_email(cls,student_email):
        internship_count = cls.query.filter_by(student_email=student_email).count()
        return internship_count

    @classmethod
    def get_already_applied(cls,student_email,internship_id):
        internship_count = cls.query.filter_by(student_email=student_email, internship_id=internship_id).all()
        return internship_count
        
    @classmethod
    def get_profile_by_MSME_email(cls,internship_email):
        internship_obj = cls.query.filter_by(internship_email=internship_email).all()
        mentornships = []

        for w in internship_obj:
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


# get all applied internships
    @classmethod
    def get_all_applied(cls,user_id):
        internship_obj = cls.query.outerjoin(Internship, Internship.id ==cls.internship_id ).all()
        mentornships = []

        for w in internship_obj:
            mentornships.append(w.json())
        
        return mentornships
