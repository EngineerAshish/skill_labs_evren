from flask import Blueprint , request
from flask_cors import CORS
from controllers import working_professional
from utils.security import token_required
cors = CORS()

working_professional_page = Blueprint('working_professional',__name__ )

cors.init_app(working_professional_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@working_professional_page.route('/api/working_professional/create_profile', methods=["POST"])
@token_required
def create_profile(user):
    request.json["email"] = user.email
    request.json["user_id"] = user.id
    return working_professional.create_working_professional_profile(request.json)

@working_professional_page.route('/api/working_professional/get_profile', methods=["GET"])
@token_required
def get_profile(user):
    return working_professional.get_profile(user)

