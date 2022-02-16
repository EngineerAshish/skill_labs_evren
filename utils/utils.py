import string
from tokenize import Number

from flask import jsonify


class Response:

    @classmethod
    def send_response(code:Number, data:object,message:string, err:string):
        response = {
            'message':message,
            'data': data,
            'error':err
        }
        return jsonify(response), code