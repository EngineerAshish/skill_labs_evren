from flask import Blueprint , request
from flask_cors import CORS
from controllers import working_professional
from utils.security import token_required, working_professional_token_required
cors = CORS()

working_professional_page = Blueprint('working_professional',__name__ )

cors.init_app(working_professional_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@working_professional_page.route('/api/working_professional/create_profile', methods=["POST"])
@working_professional_token_required
def create_profile(user):
    request.json["email"] = user.email
    request.json["user_id"] = user.id
    return working_professional.create_working_professional_profile(request.json)

@working_professional_page.route('/api/working_professional/react_mentornship', methods=["POST"])
@working_professional_token_required

def react_mentornship(user):
    request.json["email"] = user.email
    request.json["user_id"] = user.id
    return working_professional.react_mentornship(request.json)

@working_professional_page.route('/api/working_professional/get_profile', methods=["GET"])
@working_professional_token_required

def get_profile(user):
    return working_professional.get_profile(user)

@working_professional_page.route('/api/working_professional/all_mentornship_request', methods=["GET"])
@working_professional_token_required

def get_mentornship_requests(user):
    return working_professional.all_mentornship_request(user)


