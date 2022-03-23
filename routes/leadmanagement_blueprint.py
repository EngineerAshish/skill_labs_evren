from crypt import methods
from flask import Blueprint, request
from flask_cors import CORS
from controllers.leadmanagement import create_lead, dropdown_decider
from database.models.leadmanagement import leadmanagement


cors=CORS()

leadmanagement_page=Blueprint("leadmanagement",__name__)
cors.init_app(leadmanagement_page,resources={r"/*": {"origins": "*", "supports_credentials": True}})

@leadmanagement_page.route("/api/leadmanagement/new_lead",methods=["POST"])
def create_new_lead():
    return create_lead()