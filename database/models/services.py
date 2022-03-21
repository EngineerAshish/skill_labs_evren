from controllers.services import delete_service
from ..db import db

class services(db.Model):
    ser_category = db.Column(db.String(100))
    ser_sub_category = db.Column(db.String(100))
    ser_name = db.Column(db.String(100))
    ser_desc = db.Column(db.String(200))
    ser_id = db.Column(db.Integer(200))
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def commit_changes(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
    @classmethod
    def get_service_by_id(cls,ser_id):
        return cls.query.filter_by(ser_id=ser_id).first()
