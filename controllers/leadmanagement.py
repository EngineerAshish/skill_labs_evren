from turtle import pen
from database.models.leadmanagement import leadmanagement,new,assigned,pending,converted,rejected

def create_lead (data):
    leadmanagement.category=data["category"]
    leadmanagement.name=data["name"]
    leadmanagement.sub_category=data["sub_category"]
    leadmanagement.email=data["email"]
    leadmanagement.phone_number=data["phone_number"]
    leadmanagement.service_name=data["service_name"]
    leadmanagement.status=data["status"]
    leadmanagement.id=data["id"]
    leadmanagement.assigned_to=data["assigned_to"]
    leadmanagement.save_user()


def dropdown_decider(data):
    lead=leadmanagement.get_lead_by_id(data["id"])
    if not lead.assigned_to :
        new.category=data["category"]
        new.name=data["name"]
        new.sub_category=data["sub_category"]
        new.email=data["email"]
        new.phone_number=data["phone_number"]
        new.service_name=data["service_name"]
        new.status=data["status"]
        new.id=data["id"]
        new.assigned_to=data["assigned_to"]
        new.save_user()
    else:
        assigned.category=data["category"]
        assigned.name=data["name"]
        assigned.sub_category=data["sub_category"]
        assigned.email=data["email"]
        assigned.phone_number=data["phone_number"]
        assigned.service_name=data["service_name"]
        assigned.status=data["status"]
        assigned.id=data["id"]
        assigned.assigned_to=data["assigned_to"]
        assigned.save_user()
    if lead.status == 0:
        pending.category=data["category"]
        pending.name=data["name"]
        pending.sub_category=data["sub_category"]
        pending.email=data["email"]
        pending.phone_number=data["phone_number"]
        pending.service_name=data["service_name"]
        pending.status=data["status"]
        pending.id=data["id"]
        pending.assigned_to=data["assigned_to"]
        pending.save_user()
    elif lead.status==1:
        converted.category=data["category"]
        converted.name=data["name"]
        converted.sub_category=data["sub_category"]
        converted.email=data["email"]
        converted.phone_number=data["phone_number"]
        converted.service_name=data["service_name"]
        converted.status=data["status"]
        converted.id=data["id"]
        converted.assigned_to=data["assigned_to"]
        converted.save_user()
    elif lead.status==2:
        rejected.category=data["category"]
        rejected.name=data["name"]
        rejected.sub_category=data["sub_category"]
        rejected.email=data["email"]
        rejected.phone_number=data["phone_number"]
        rejected.service_name=data["service_name"]
        rejected.status=data["status"]
        rejected.id=data["id"]
        rejected.assigned_to=data["assigned_to"]
        rejected.save_user()
