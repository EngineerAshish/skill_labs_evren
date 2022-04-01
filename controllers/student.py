from distutils.command.config import config
from urllib import response
from flask import jsonify
from database.models.Student import Student
from database.models.Mentornship import Mentornship
from database.models.User import User as User_model
from database.models.Internship import Internship as Internship_model
from database.models.intern import Intern as Intern_model

from database.models.Working_professional import Working_professional
from utils.config import User, abb
from utils.utils import Response
# from cerberus import Validator, errors
# from schema.student_profile import schema as student_profile_schema

# class CustomErrorHandler(errors.BasicErrorHandler):
#     messages = errors.BasicErrorHandler.messages.copy()
#     messages[errors.FORBIDDEN_VALUE.code] = 'VERBOTEN!'

def create_student_profile(data):
    try:
        # v = Validator(student_profile_schema,error_handler=CustomErrorHandler)
        # if not v.validate(data):
        #     print(v.errors)
        #     return Response.send_respose(401, {}, 'unsuccessful post', 'schema validation failed')
        get_profile = Student.get_profile_by_email(data["email"])
        if not get_profile:
            return Response.send_respose(404, {}, 'user is not a student', 'not found')  
        get_profile.user_id = data["user_id"]
        get_profile.tenth_name = data["tenth_name"]
        get_profile.tenth_marks = data["tenth_marks"]
        get_profile.twelfth_name = data["twelfth_name"]
        get_profile.twelfth_marks = data["twelfth_marks"]
        get_profile.UG_degree = data["UG_degree"]
        get_profile.UG_marks = data["UG_marks"]
        get_profile.UG_institution_name = data["UG_institution_name"]
        get_profile.PG_degree = data["PG_degree"]
        get_profile.PG_marks = data["PG_marks"]
        get_profile.PG_institution_name = data["PG_institution_name"]
        get_profile.intrested_areas = data["intrested_areas"]

        get_profile.save_profile()
        return Response.send_respose(200,data, 'successful post', '')

    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

def get_Student_profile(user):
    try:
        get_student = Student.get_profile_by_email(user.email)
        if not get_student:
            return Response.send_respose(404, {}, 'user is not a student', 'not found')  
        return Response.send_respose(200, {"profile_data":get_student.json(), "user_data":user.json()},'', '' )
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

def get_mentors(user,page=1):
    try:
        print(f"page is {page}")
        working_professionals = Working_professional.get_working_professionals(int(page),user.email)
        return Response.send_respose(200, working_professionals, '', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')



def add_mentor(data):
    try:
        working_professional = Working_professional.get_user_by_id(data["mentornship"]["mentor_id"])
        if not working_professional:
            return Response.send_respose(404, {}, 'user is not a working professional', 'not found') 

        working_professional_user = User_model.get_user_by_email(working_professional.email)
        if not working_professional:
            return Response.send_respose(404, {}, 'no such mentor found', 'no such mentor found')
        already_request = Mentornship.get_if_already_requested(data["user"].id,working_professional.id)
        
        if already_request:
            return Response.send_respose(404, {}, 'request already sent', 'duplicate request') 
        post_data = {
            "student_id": data["user"].id,
            "working_professional_id": working_professional.id,
            "student_name":data["user"].name,
            "student_email":data["user"].email,
            "mentor_name": working_professional_user.name,
            "mentor_email": working_professional.email,
            "status":abb.mentornship.pending
        }
        mentornship = Mentornship(**post_data)
        mentornship.save_profile()
        return Response.send_respose(200, post_data, '', '')

    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

def get_all_mentornship(data):
    try:
        get_mentornships = Mentornship.get_mentornships_by_student_email(data.email)
        return Response.send_respose(200, get_mentornships, '', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')
    

def apply_intership(data):
    try:
        student_profile = Student.get_profile_by_email(data["user"].email)
        student_profile_status= student_profile.json()["profile_completed"]
        if student_profile_status < 100.00:
          return Response.send_respose(400, {}, f"please complete your profile {student_profile_status}", 'profile not complete')
        get_internship = Internship_model.get_profile_by_id(data["internship"]["internship_id"])
        if not get_internship:
          return Response.send_respose(400, {}, f"no internship with id ", 'not found')
        # check already applied 
        get_applied = Intern_model.get_already_applied(data["user"].email, data["internship"]["internship_id"])
        if get_applied:
            return Response.send_respose(400, {}, f"already applied to this internship", 'cant apply more than 1')

        #   check the count of the interships

        Internship_count = Intern_model.get_count_by_MSME_email(data["user"].email)
        if Internship_count>=5:
            return Response.send_respose(400, {}, f"apply threshold breached {Internship_count}", 'cant apply more than 5')

        print(f"=====================>>>>>>>>{Internship_count}")
        post_intern = Intern_model()
        post_intern.internship_company_name = get_internship.MSME_name
        post_intern.internship_email = get_internship.email
        post_intern.internship_id = get_internship.id
        post_intern.internship_name = get_internship.requirement_title
        post_intern.valid_till = "2022-03-30 04:30:52"
        post_intern.status = User.Intern.intern_pending
        post_intern.student_email = data["user"].email
        post_intern.student_id = data['user'].id
        post_intern.save_profile()
        return Response.send_respose(200, {}, 'sucessfull post', '')
        
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

def recommend_internship(**data):
    try:
        student = Student.get_profile_by_email(data["user"].email)
        get_insternships = Internship_model.get_student_insternship(student.intrested_areas, data["page"])
        return Response.send_respose(200, get_insternships, 'sucessfull post', '')
        
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

def get_all_applied_internship(user):
    try:
        get_internships = Internship_model.get_all_applied(user.id)
        return Response.send_respose(200, get_internships, 'sucessfull get', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

def get_all_not_applied_internship(user):
    try:
        get_internships = Internship_model.get_all_not_applied(user.id)
        return Response.send_respose(200, get_internships, 'sucessfull get', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')
