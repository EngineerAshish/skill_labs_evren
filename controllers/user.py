from datetime import datetime
from urllib import response
from cerberus import Validator
from pymysql import IntegrityError
from utils.utils import Response
from flask_mail import Mail,Message
from database.models.Otp import Otp
from werkzeug.security import safe_str_cmp
from utils.security import create_user_token
from sqlalchemy import exc
import os
# schemas
from schema.user_registration import schema as register_schema
from schema.OTP_login import schema as otp_schema

from database.models.User import User
from database.models.Student import Student
from database.models.Working_professional import Working_professional
from database.models.MSME import MSME

from utils.config import User as user_variable

# instantiate Mail object
mail = Mail()

# instantiate response object
response_obj = Response()

def post_user(data):
    try:
        old_user = User.get_user_by_email(data["email"])
        if old_user:
            return response_obj.send_respose(400, {}, 'unSuccessful signUp','email has to be unique')
        v = Validator(register_schema)

        # if not v.validate(data):
        #     return response_obj.send_respose(400, {}, 'unSuccessful signUp','schema validation failed')
        new_user = {
            "name":data["name"],
            "email":data["email"],
            "phone_number":data["phone_number"],
            "profile_image":data["profile_image"],
            "active":user_variable.inactive,
            "category":data["category"]
        }
        post_user = User(**new_user)

        # current_user = User.get_user_by_email(data["email"])
        if data["category"] == user_variable.student:
            if data["type"]!=1 and data["type"]!=2:
                return response_obj.send_respose(400, {}, 'unSuccessful signUp','user type has to be either intern or other services')
            data["category"] = user_variable.student
            post_student = Student()
            # post_student.user_id = current_user.id
            post_student.college = data["college"]
            post_student.location = data["location"]
            post_student.highest_qualification = data["highest_qualification"]
            post_student.type = 1
            post_student.email = data["email"]
            post_student.save_profile()


        if data["category"] == user_variable.working_professional:
            if data["type"]!=1 and data["type"]!=2:
                return response_obj.send_respose(400, {}, 'unSuccessful signUp','user type has to be either mentor or other services')
            data["category"] = user_variable.working_professional
            post_working_experience = Working_professional()
            # post_working_experience.user_id = current_user.id
            post_working_experience.email = data["email"]
            post_working_experience.type = data["type"]
            post_working_experience.designation = data["designation"]
            post_working_experience.location = data["location"]
            post_working_experience.current_company = data["current_company"]
            post_working_experience.save_user()

        if data["category"] == user_variable.MSME_user:
            print("inside msme")
            if data["type"]!=1 and data["type"]!=2:
                return response_obj.send_respose(400, {}, 'unSuccessful signUp','user type has to be either mentor or other services')
            post_MSME = MSME()

            post_MSME.email = data["email"]
            post_MSME.business_category = data["business_category"]
            post_MSME.business_type = data["business_type"]
            post_MSME.location = data["location"]
            post_MSME.type = data["type"]
            post_MSME.save_user()

        
        post_user.save_user()
        
        return response_obj.send_respose(200, data, 'successful signUp','')
    except Exception as e:
        print(e)
        return response_obj.send_respose(500, {}, 'unsuccessful signUp',str(e))

        
def send_otp(data):
    try:
        user = User.get_user_by_email(data["email"])
        if not user:
            return response_obj.send_respose(404, {}, 'user not found','please check the email')

                # delete already existing otps
        Otp.delete_many(user.email)

        # generate 5 digit random number
        generate_otp =  Otp.create_otp()

        # creating otp validate time (5 min = 300 sec)
        validity = Otp.create_validity()

        # create Otp object and save it to db
        otp = Otp(user_id=user.id,email = user.email, OTP=generate_otp,valid_till=validity)

        otp.save_otp()    

        msg = Message(
        f'Skill Lab Email Verefication',
        sender =os.environ.get("EMAIL"),
        recipients = [user.email]
        )
        msg.body = f'Hello your otp is {generate_otp}'
        mail.send(msg)

        return response_obj.send_respose(200, {"email": user.email}, 'successful otp sent','')
    except:
        return response_obj.send_respose(500, {"email": user.email}, 'unSuccessful otp sent','internal server error')

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
            # bypass login
            if safe_str_cmp("1111",data["OTP"]) and safe_str_cmp("sameervashisht39@gmail.com",data["email"]):
                get_user = User.get_user_by_email(data["email"])
                token = create_user_token(get_user)
                return response_obj.send_respose(200,{"access_token":token, "role": who_login(get_user.category)},'Successful verification','')

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
                
                get_user = User.get_user_by_email(data["email"])
                token = create_user_token(get_user)
                otp.delete_otp()
                return response_obj.send_respose(200,{"access_token":token ,"role": who_login(get_user.category)},'Successful verification','')

            else:
                return response_obj.send_respose(200,{},'unSuccessful verification','no OTP found')
                
        except Exception as e:
            print(e)
            return response_obj.send_respose(500, {}, 'unSuccessful signUp','internal server error')

def who_login(type):
    if type == user_variable.student:
        return "student"
    if type == user_variable.working_professional:
        return "working professional"