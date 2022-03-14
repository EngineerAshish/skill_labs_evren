from ast import Num
from tokenize import Number
from typing import Dict


from flask import jsonify, make_response
from itsdangerous import json

from sqlalchemy.inspection import inspect



class Response:

    @classmethod
    def send_respose(self,code:Num,data:Dict, message:str, err:str ):
        response = {
            'message':message,
            'data':data,
            'error':err
        }
        return jsonify(response), code


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]