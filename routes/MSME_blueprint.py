from controllers.MSME import create_MSME_profile, get_MSME_profile, create_internship,get_internships_created, get_interns_applied, react_internship
from flask import Blueprint, request
from utils.security import token_required, MSME_token_required

from flask_cors import CORS

cors = CORS()

MSME_page = Blueprint('MSME',__name__ )

cors.init_app(MSME_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@MSME_page.route("/api/MSME/create_profile", methods=["POST"])
@MSME_token_required
def user_signIn(user):
    request.json["email"] = user.email
    request.json["user_id"] = user.id
    return create_MSME_profile(request.json)

@MSME_page.route("/api/MSME/create_internship", methods=["POST"])
@MSME_token_required

def create_internship_MSME(user):
    return create_internship({"user":user, "internship":request.json})

@MSME_page.route("/api/MSME/get_profile", methods=["GET"])
@MSME_token_required

def get_profile(user):
    return get_MSME_profile(user)

@MSME_page.route("/api/MSME/get_internships", methods=["GET"])
@MSME_token_required

def get_internships(user):
    return get_internships_created(user)

@MSME_page.route("/api/MSME/get_interns", methods=["GET"])
@MSME_token_required

def get_interns(user):
    return get_interns_applied(user)


@MSME_page.route("/api/MSME/react_internship", methods=["POST"])
@MSME_token_required

def react_internship_MSME(user):
    return react_internship({"user":user, "internship":request.json})