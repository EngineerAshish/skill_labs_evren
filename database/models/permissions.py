from datetime import datetime
from sqlalchemy import true
from database.models.User import User
from ..db import db

class permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    viewEStu=db.Column(db.Boolean(), default=False)
    viewEMent=db.Column(db.Boolean(), default=False)
    viewEMsme=db.Column(db.Boolean(), default=False)
    viewNortif=db.Column(db.Boolean(), default=False)
    createNortif=db.Column(db.Boolean(), default=False)
    viewServices=db.Column(db.Boolean(), default=False)
    createServices=db.Column(db.Boolean(), default=False)
    assignServices=db.Column(db.Boolean(), default=False)
    viewNewLeades=db.Column(db.Boolean(), default=False)
    viewPendingLeades=db.Column(db.Boolean(), default=False)
    viewConvertedLeades=db.Column(db.Boolean(), default=False)
    viewReports=db.Column(db.Boolean(), default=False)
    created_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
    updated_dt = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False,onupdate=datetime.utcnow())


    def save_permissions(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_user_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    

