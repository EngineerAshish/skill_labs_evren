from datetime import datetime
from urllib import response
from cerberus import Validator
from utils.utils import Response
from flask_mail import Mail,Message
from database.models.Otp import Otp
from werkzeug.security import safe_str_cmp

import os
# schemas
from schema.user_registration import schema as register_schema
from schema.OTP_login import schema as otp_schema

from database.models.User import User

from utils.config import User as user_variable

# instantiate Mail object
mail = Mail()

# instantiate response object
response_obj = Response()

def post_user(data):
    try:

        v = Validator(register_schema)

        if not v.validate(data):
            return response_obj.send_respose(400, {}, 'unSuccessful signUp','schema validation failed')
        
        data["category"] = user_variable.student
        data["active"] = user_variable.inactive

        post_user = User(**data)
        post_user.save_user()
        return response_obj.send_respose(200, data, 'successful signUp','')
    except Exception as e:
        print(e)
        return response_obj.send_respose(500, {}, 'successful signUp','internal server error')

        
def send_otp(data):
    try:
        if data["user"] == "student":
            student = User.get_user_by_email(data["email"])
            if not student:
                return response_obj.send_respose(404, {}, 'user not found','please check the email')

                    # delete already existing otps
            Otp.delete_many(student.email)

            # generate 5 digit random number
            generate_otp =  Otp.create_otp()

            # creating otp validate time (5 min = 300 sec)
            validity = Otp.create_validity()

            # create Otp object and save it to db
            otp = Otp(user_id=student.id,email = student.email, OTP=generate_otp,valid_till=validity)

            otp.save_otp()    

            msg = Message(
            f'Skill Lab Email Verefication',
            sender =os.environ.get("EMAIL"),
            recipients = [student.email]
            )
            msg.body = f'Hello your otp is {generate_otp}'
            mail.send(msg)

            return response_obj.send_respose(200, {"email": student.email}, 'successful otp sent','')
    except:
        return response_obj.send_respose(500, {"email": student.email}, 'unSuccessful otp sent','internal server error')
    return response_obj.send_respose(500, {}, 'successful signUp','internal server error')

# create and save otp
def save_otp(user:User):
    # generate 5 digit random number
    generate_otp =  Otp.create_otp()

    # creating otp validate time (5 min = 300 sec)
    validity = Otp.create_validity()

    # create Otp object and save it to db
    otp = Otp(user_id=user.id,email = user.email, OTP=generate_otp,valid_till=validity)

    otp.save_otp()

    return generate_otp


def login(data):
    v = Validator(otp_schema)
    if v.validate(data):
        try:
            otp = Otp.get_by_email(data["email"])
            # check if there is a otp in db associated with email
            if(otp):
                # check if the otp has expired
                if otp.valid_till<datetime.now():
                    otp.delete_otp()
                    return response_obj.send_respose(200,{},'unSuccessful verification','OTP expired')
                
                # comparing the use input with the otp from db
                if not safe_str_cmp(otp.OTP,data["OTP"]):
                    return response_obj.send_respose(200,{},'unSuccessful verification','OTP didnt match')
                
                return response_obj.send_respose(200,{},'Successful verification','')
            else:
                return response_obj.send_respose(200,{},'unSuccessful verification','no OTP found')
                
        except Exception as e:
            print(e)
            return response_obj.send_respose(500, {}, 'unSuccessful signUp','internal server error')

            