from database.models.Working_professional import Working_professional
from utils.utils import Response

def create_working_professional_profile(data):
    try:
        working_professional = Working_professional.get_user_by_email(data["email"])
        working_professional.PG_degree = data["PG_degree"]
        working_professional.UG_degree = data["UG_degree"]
        working_professional.current_company = data["current_company"]
        working_professional.working_experience = data["working_experience"]
        working_professional.intrested_area = data["intrested_area"]
        working_professional.organisation = data["organisation"]
        working_professional.user_id= data["user_id"]
        working_professional.save_user()
        return Response.send_respose(200, working_professional.json(), 'profile created', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'something went wrong', 'Internal server error')

def get_profile(email):
    try:
        working_professional = Working_professional.get_user_by_email(email)
        return Response.send_respose(200, working_professional.json(), 'profile', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'something went wrong', 'Internal server error')   
 