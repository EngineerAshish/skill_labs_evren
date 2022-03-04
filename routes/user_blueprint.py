from controllers.user import post_user, send_otp, login
from flask import Blueprint, request


from flask_cors import CORS

cors = CORS()

user_page = Blueprint('user',__name__ )

cors.init_app(user_page, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@user_page.route("/api/users/signUp", methods=["POST"])
def user_signIn():
    return post_user(request.json)

@user_page.route("/api/users/hello", methods=["GET"])
def hello_user():
    return "hello"

@user_page.route("/api/users/send_otp", methods=["Post"])
def send_otp_signIn():
    return send_otp({"email":request.args.get("email")})

@user_page.route("/api/users/login", methods=["post"])
def login_user():
    return login(request.json)