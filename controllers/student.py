from database.models.Student import Student
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
        post_user_profile = Student(**data)
        post_user_profile.save_profile()
        return Response.send_respose(200, data, 'successful post', '')

    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')
