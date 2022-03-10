from controllers.MSME import create_MSME_profile, get_MSME_profile, create_internship
from flask import Blueprint, request
from utils.security import token_required

from flask_cors import CORS

cors = CORS()

MSME_page = Blueprint('MSME',__name__ )

cors.init_app(MSME_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@MSME_page.route("/api/MSME/create_profile", methods=["POST"])
@token_required
def user_signIn(user):
    request.json["email"] = user.email
    request.json["user_id"] = user.id
    return create_MSME_profile(request.json)

@MSME_page.route("/api/MSME/create_internship", methods=["POST"])
@token_required
def create_internship_MSME(user):
    return create_internship({"user":user, "internship":request.json})

@MSME_page.route("/api/MSME/get_profile", methods=["GET"])
@token_required
def get_profile(user):
    return get_MSME_profile(user)


