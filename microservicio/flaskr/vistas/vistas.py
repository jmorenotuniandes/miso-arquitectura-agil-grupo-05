from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import time
from random import randrange
import logging
import sys

class VistaPing(Resource):

    def get(self):
        
        # create logger
        logger = logging.getLogger('LlamadaMicroservicio')
        logger.setLevel(logging.DEBUG)
        logger.flush = sys.stdout.flush

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        #Fuente errores comunes: https://kb.iu.edu/d/bfrc
        erroCodes = [0, 200, 400, 200, 401, 200, 403, 200, 404, 200, 405, 200, 406, 200, 408, 200, 409, 200, 500, 200, 503, 200, 504, 200, 505, 200]
        responseIndex = randrange(27)
        errorCode = erroCodes[responseIndex]
        responseText = 'OK'
        if(responseIndex == 0): #Cero representa un tiempo de respuesta largo para que de timeout
            time.sleep(20)
            errorCode = 200
            responseText = "Tiempo de respuesta largo"

        if(errorCode != 200):
            responseText = 'Error en la aplicacion'
        
        logger.debug(str(errorCode) + ' ' + responseText )
        logger.removeHandler(ch)
        
        return responseText, errorCode
