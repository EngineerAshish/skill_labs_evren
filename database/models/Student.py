from datetime import datetime
from ..db import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)
    college = db.Column(db.String(100))
    location = db.Column(db.String(100))
    highest_qualification = db.Column(db.String(100))
    # category = db.Column(db.Integer)  
    tenth_marks = db.Column(db.DECIMAL(19, 4))
    tenth_name = db.Column(db.String(100))
    twelfth_marks = db.Column(db.DECIMAL(19, 4))
    twelfth_name = db.Column(db.String(100))
    UG_marks = db.Column(db.DECIMAL(19, 4))
    UG_degree = db.Column(db.String(100))
    UG_institution_name = db.Column(db.String(100))
    PG_marks = db.Column(db.DECIMAL(19, 4))
    PG_degree = db.Column(db.String(100))
    PG_institution_name = db.Column(db.String(100))
    intrested_areas = db.Column(db.String(100))
    created_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
    updated_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False,onupdate=datetime.utcnow())
    

    def json(self):
        self_dict = self.__dict__
        user_dict = {x:self_dict[x] for x in self_dict.keys() if not x.startswith("_") and x!="enc_password"}
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