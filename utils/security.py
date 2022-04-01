from datetime import datetime, timedelta
from functools import wraps
import imp
import os
from flask import jsonify, request
import jwt
from database.models.User import User
from .utils import Response
from .config import User as User_var
def create_user_token(user):
    # creating jwt token 
    token = jwt.encode({
        "user_id":user.id,
        "email":user.email,
        'exp' : datetime.utcnow() + timedelta(minutes = 30)
    },os.environ.get("SECRET_KEY_USER"))
    return token.decode('UTF-8')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        #jwt is sent by headers
        if 'access_token' in request.headers:
            token = request.headers['access-token']
            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, os.environ.get("SECRET_KEY_USER"))
                current_user = User.get_user_by_id(data["user_id"])
                # check if user is blocked 
                if current_user.active == 2:
                    return jsonify({
                    'message' : 'user is blocked by admin !!',
                }), 401
            except:
                return jsonify({
                    'message' : 'Token is invalid !!',
                }), 401
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401    
        return f(current_user,*args, **kwargs)
    return decorated    

def student_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        #jwt is sent by headers
        if 'access_token' in request.headers:
            token = request.headers['access-token']
            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, os.environ.get("SECRET_KEY_USER"))
                current_user = User.get_user_by_id(data["user_id"])
                # check if user is blocked 
                if current_user.active == 2:
                    return jsonify({
                    'message' : 'user is blocked by admin !!',
                }), 401

                # check if the user is student or not 
                if current_user.category!= User_var.student:
                    return jsonify({
                    'message' : 'User is not a student!!',
                }), 401
            except:
                return jsonify({
                    'message' : 'Token is invalid !!',
                }), 401
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401    
        return f(current_user,*args, **kwargs)
    return decorated    

def working_professional_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        #jwt is sent by headers
        if 'access_token' in request.headers:
            token = request.headers['access-token']
            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, os.environ.get("SECRET_KEY_USER"))
                current_user = User.get_user_by_id(data["user_id"])
                # check if user is blocked 
                if current_user.active == 2:
                    return jsonify({
                    'message' : 'user is blocked by admin !!',
                }), 401

                # check if the user is student or not 
                if current_user.category!= User_var.working_professional:
                    return jsonify({
                    'message' : 'User is not a working_professional!!',
                }), 401
            except:
                return jsonify({
                    'message' : 'Token is invalid !!',
                }), 401
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401    
        return f(current_user,*args, **kwargs)
    return decorated    


def MSME_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        #jwt is sent by headers
        if 'access_token' in request.headers:
            token = request.headers['access-token']
            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, os.environ.get("SECRET_KEY_USER"))
                current_user = User.get_user_by_id(data["user_id"])
                # check if user is blocked 
                if current_user.active == 2:
                    return jsonify({
                    'message' : 'user is blocked by admin !!',
                }), 401

                # check if the user is student or not 
                if current_user.category!= User_var.MSME_user:
                    return jsonify({
                    'message' : 'User is not a MSME!!',
                }), 401
            except:
                return jsonify({
                    'message' : 'Token is invalid !!',
                }), 401
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401    
        return f(current_user,*args, **kwargs)
    return decorated    

