from crypt import methods
from flask import Blueprint, request
from flask_cors import CORS
from controllers.services import view_service,create_service,update_service,delete_service
from database.models.services import services


cors=CORS()

services_page=Blueprint("services",__name__)
cors.init_app(services_page,resources={r"/*": {"origins": "*", "supports_credentials": True}})

@services_page.route("/api/services/new_service",methods=["POST"])
def create_new_services():
    return create_service()

    
@services_page.route("/api/services/update_service",methods=["UPDATE"])
def update_services():
    return update_service()

@services_page.route("/api/services/delete_service",methods=["DELETE"])
def delete_services():
    return delete_service()

@services_page.route("/api/services/view_service/<service_id>",methods=["GET"])
def view_services():
    return view_service(service_id)

