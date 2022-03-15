from database.models.User import User
from database.models.permmissions import permissions
from flask import Flask,redirect,url_for

@app.route ('/noaccess')
def noaccess():
    return "you are not allowed to access the page"

# user = permissions.get_user_by_id()  #how to get the user using it for global use

def viewEStu():
    if user.viewEStu == False:
        return redirect(url_for('noaccess'))
def viewEMent():
    if user.viewEMent == False:
        return redirect(url_for('noaccess'))
def viewEMsme():
    if user.viewEMsme == False:
        return redirect(url_for('noaccess'))
def viewNortif():
    if user.viewNortif == False:
        return redirect(url_for('noaccess'))
def createNortif():
    if user.createNortif == False:
        return redirect(url_for('noaccess'))
def viewServices():
    if user.viewServices == False:
        return redirect(url_for('noaccess'))
def createServices():
    if user.createServices == False:
        return redirect(url_for('noaccess'))
def assignServices():
    if user.assignServices == False:
        return redirect(url_for('noaccess'))
def viewNewLeades():
    if user.viewNewLeades == False:
        return redirect(url_for('noaccess'))
def viewPendingLeades():
    if user.viewPendingLeades == False:
        return redirect(url_for('noaccess'))
def viewConvertedLeads():
    if user.viewConvertedLeades == False:
        return redirect(url_for('noaccess'))
def viewReports():
    if user.viewReports == False:
        return redirect(url_for('noaccess'))

def post_access_type(data):
    user = User.get_user_by_id(data["id"])
    

