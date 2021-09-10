from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import time
from random import randrange
import logging
import sys

class VistaMonitorRegistroPaciente(Resource):

    def get(self):

        
        return 'OK', 200
