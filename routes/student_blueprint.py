from controllers.student import create_student_profile
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