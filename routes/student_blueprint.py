from controllers.student import create_student_profile, get_Student_profile, get_mentors, add_mentor
from flask import Blueprint, request
from utils.security import token_required

from flask_cors import CORS

cors = CORS()

student_page = Blueprint('student',__name__ )

cors.init_app(student_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@student_page.route("/api/student/create_profile", methods=["POST"])
@token_required
def user_signIn(user):
    request.json["email"] = user.email
    request.json["user_id"] = user.id
    return create_student_profile(request.json)

@student_page.route("/api/student/get_profile", methods=["GET"])
@token_required
def get_profile(user):
    return get_Student_profile(user)

@student_page.route("/api/student/add_mentor", methods=["POST"])
@token_required
def add_mentor_by_student(user):
    return add_mentor({"user":user, "mentornship":request.json})

@student_page.route("/api/student/get_mentors", methods=["GET"])
def get_mentors_to_mentor():
    return get_mentors(page = request.args.get("page"))