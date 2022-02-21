from urllib import response
from cerberus import Validator
from utils.utils import Response
response_obj = Response()
# schemas
from schema.user_registration import schema as register_schema

def post_user(data):
    v = Validator(register_schema)

    if not v.validate(data):
        return response_obj.send_respose(400, {}, 'unSuccessful signUp','schema validation failed')
        
    return response_obj.send_respose(200, {}, 'successful signUp','')

    