from database.models.ins_org import ins_org
from utils.utils import Response


def create_ins_org(data):
    try:
        ins_org.ins_org_name=data["ins_org_name"]
        ins_org.ins_org_state=data["ins_org_state"]
        ins_org.ins_org_city=data["ins_org_city"]
        ins_org.save_user()
        return Response.send_respose(200, data, 'institute created', '')
    except Exception as e:
        print(e)
        return Response.send_respose(500, {}, 'something went wrong', 'Internal server error')
