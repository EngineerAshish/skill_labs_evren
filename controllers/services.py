from controllers.permissions import permission
from database.models.services import services
from utils.utils import Response

def create_service(data):
    try:
        services.ser_category=data["ser_category"]
        services.ser_desc=data["ser_desc"]
        services.ser_name=data["ser_name"]
        services.ser_sub_category=data["ser_sub_category"]
        services.save_user()       
        return Response.send_respose(200, data, 'service created', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'something went wrong', 'Internal server error')


def update_service(data):
    
    try:
        user=services.get_service_by_id(data["ser_id"])
        user.ser_category=data["ser_category"]
        user.ser_desc=data["ser_desc"]
        user.ser_name=data["ser_name"]
        user.ser_sub_category=data["ser_sub_category"]
        user.ser_id=data["ser_id"]
        services.commit_changes(user)
        return Response.send_respose(200, data, 'service updated', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'something went wrong', 'Internal server error')



def view_service(data):
    
    try:
        user=services.get_service_by_id(data["ser_id"])
        return user
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'something went wrong', 'Internal server error')



def delete_service(data):
    
    try:
        user=services.get_service_by_id(data["ser_id"])
        services.delete(user)
        return Response.send_respose(200, data, 'service deleted', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'something went wrong', 'Internal server error')
