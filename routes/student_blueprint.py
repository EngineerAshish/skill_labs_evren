from controllers.student import create_student_profile, get_Student_profile, get_mentors, add_mentor, get_all_mentornship,apply_intership, recommend_internship
from controllers import student
from flask import Blueprint, request
from utils.security import token_required, student_token_required

from flask_cors import CORS

cors = CORS()

student_page = Blueprint('student',__name__ )

cors.init_app(student_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@student_page.route("/api/student/create_profile", methods=["POST"])
@student_token_required
def user_signIn(user):
    request.json["email"] = user.email
    request.json["user_id"] = user.id
    return create_student_profile(request.json)

@student_page.route("/api/student/get_profile", methods=["GET"])
@student_token_required
def get_profile(user):
    return get_Student_profile(user)

@student_page.route("/api/student/add_mentor", methods=["POST"])
@student_token_required
def add_mentor_by_student(user):
    return add_mentor({"user":user, "mentornship":request.json})

@student_page.route("/api/student/apply_internship", methods=["POST"])
@student_token_required
def apply_interships(user):
    return apply_intership({"user":user, "internship":request.json})


@student_page.route("/api/student/get_mentors", methods=["GET"])
@student_token_required
def get_mentors_to_mentor(user):
    return get_mentors(user,page = request.args.get("page"))

@student_page.route("/api/student/get_mentornships", methods=["GET"])
@student_token_required
def get_mentornships(user):
    return get_all_mentornship(user)


@student_page.route("/api/student/get_applied_internship", methods=["GET"])
@student_token_required
def get_applied_internship(user):
    return student.get_all_applied_internship(user)

@student_page.route("/api/student/get_not_applied_internship", methods=["GET"])
@student_token_required
def get_not_applied_internship(user):
    return student.get_all_not_applied_internship(user)

@student_page.route("/api/student/recommend_internship", methods=["GET"])
@student_token_required

def get_internship_recommendations(user):
    return recommend_internship(user = user, page = int(request.args.get("page")))