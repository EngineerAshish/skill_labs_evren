from utils.config import User
from database.models.MSME import MSME
from utils.utils import Response

def create_MSME_profile(data):
    try:
        get_profile = MSME.get_user_by_email(data["email"])
        if not get_profile:
            return Response.send_respose(404, {}, 'user is not a working professional', 'not found')
        get_profile.user_id = data["user_id"]
        get_profile.business_category = data["business_category"]
        get_profile.business_type = data["business_type"]
        get_profile.location = data["location"]
        get_profile.type = data["type"]
        get_profile.save_user()
        return Response.send_respose(200, data, 'successful post', '')

    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'unsuccessful post', 'Internal server error')

