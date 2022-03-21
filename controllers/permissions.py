from database.models.User import User
from database.models.permissions import permissions

class permission(permissions):
    def viewEStu():
        if permissions.viewEStu == False:
            return "You are not authorised "
    def viewEMent():
        if permissions.viewEMent == False:
            return "You are not authorised "
    def viewEMsme():
        if permissions.viewEMsme == False:
            return "You are not authorised "
    def viewNortif():
        if permissions.viewNortif == False:
            return "You are not authorised "
    def createNortif():
        if permissions.createNortif == False:
            return "You are not authorised "
    def viewServices():
        if permissions.viewServices == False:
            return "You are not authorised "
    def createServices():
        if permissions.createServices == False:
            return "You are not authorised "
    def assignServices():
        if permissions.assignServices == False:
            return "You are not authorised "
    def viewNewLeades():
        if permissions.viewNewLeades == False:
            return "You are not authorised "
    def viewPendingLeades():
        if permissions.viewPendingLeades == False:
            return "You are not authorised "
    def viewConvertedLeads():
        if permissions.viewConvertedLeades == False:
            return "You are not authorised "
    def viewReports():
        if permissions.viewReports == False:
            return "You are not authorised "

    def post_access_type(data):
        User = permissions.get_user_by_id(data["id"])
    

