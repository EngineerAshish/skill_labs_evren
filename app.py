from flask import Flask, jsonify
from database.db import db

import os

app = Flask(__name__)

# database configuration
# tell the location of database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("database_uri")
# turns off the flask sqlalchemy tracker ,as sqlalchemy modification tracker is better
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True

# @app.route("/", methods = ["GET"])
# def home():
#     return jsonify("hello world")

# we can create the db and tables using sql alchemy 

@app.before_first_request
def create_table():
    db.create_all()

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=os.environ.get("BACKEND_PORT"),debug=True)