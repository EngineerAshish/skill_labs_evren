from flask import Flask, jsonify
from database.db import db
from flask_mail import Mail

import os

app = Flask(__name__)

# database configuration
# tell the location of database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("database_uri")
# turns off the flask sqlalchemy tracker ,as sqlalchemy modification tracker is better
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True

# mail config
# configuration of mail
app.config['MAIL_SERVER']='smtp.office365.com'
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL")
app.config['MAIL_PASSWORD'] = os.environ.get("PASSWORD")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True 
mail= Mail()


from flask_cors import CORS

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# import blueprints
from routes.user_blueprint import user_page
from routes.student_blueprint import student_page
from routes.working_professional_blueprint import working_professional_page
from routes.MSME_blueprint import MSME_page

# register blueprints
app.register_blueprint(user_page)
app.register_blueprint(student_page)
app.register_blueprint(working_professional_page)
app.register_blueprint(MSME_page)

@app.before_first_request
def create_table():
    db.create_all()

if __name__ == "__main__":
    db.init_app(app)
    mail.init_app(app)
    app.run(host="0.0.0.0",port=os.environ.get("BACKEND_PORT"),debug=True)