from ..db import db

class ins_org(db.Model):
    ins_org_name = db.Column(db.String(100))
    ins_org_city = db.Column(db.String(100))
    ins_org_state = db.Column(db.String(100))
    def save_user(self):
        db.session.add(self)
        db.session.commit()