from webbrowser import get
from utils.config import User
from database.models.MSME import MSME
from utils.utils import Response

def create_MSME_profile(data):
    try:
        get_profile = MSME.get_user_by_email(data["email"])
        if not get_profile:
            return Response.send_respose(404, {}, 'user is not a working professional', 'not found')
        try:
            get_profile.user_id = data["user_id"]
            get_profile.business_name = data["business_name"]
            get_profile.firm_type = data["firm_type"]
            get_profile.gst_number = data["gst_number"]
            get_profile.urn_number = data["urn_number"]
            get_profile.date_of_incorporation = data["date_of_incorporation"]
            get_profile.functional_areas = data["functional_areas"]
            get_profile.upload_docs = data["upload_docs"]
            get_profile.intrested_areas  = data["intrested_areas"]
            get_profile.location = data["location"]
            get_profile.save_user()
        except Exception as e:
            print(e)
            return Response.send_respose(500, {}, 'internal server error', str(e))
 
             
            
        return Response.send_respose(200, data, 'successful post', '')

    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

def get_MSME_profile(email):
    try:
        get_MSME = MSME.get_user_by_email(email)
        if not get_MSME:
            return Response.send_respose(404, {}, 'user is not a MSME', 'not found')  
        return Response.send_respose(200, get_MSME.json(), '','')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

