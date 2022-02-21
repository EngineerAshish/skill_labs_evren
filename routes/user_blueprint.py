from controllers.user import post_user
from flask import Blueprint, request


from flask_cors import CORS

cors = CORS()

user_page = Blueprint('user',__name__ )

cors.init_app(user_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@user_page.route("/api/users/signUp", methods=["POST"])
def user_signIn():
    return post_user(request.json)