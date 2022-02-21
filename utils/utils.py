from ast import Num
from tokenize import Number
from typing import Dict


from flask import jsonify, make_response
from itsdangerous import json


class Response:

    @classmethod
    def send_respose(self,code:Num,data:Dict, message:str, err:str ):
        response = {
            'message':message,
            'data':data,
            'error':err
        }
        return jsonify(response), code