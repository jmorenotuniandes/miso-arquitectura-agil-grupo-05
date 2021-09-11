from typing import final, get_args
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from random import randrange
import requests
from datetime import datetime, date, time, timedelta
import logging
import sys

class GenerarDatos(Resource):
    def get(self):
        def verify(inicio, fin):
            while fin > datetime.now():
                try:
                    print(f'{datetime.now()}')
                    requests.get('http://localhost:4900/monitor/registropaciente')
                    requests.get('http://localhost:4901/registropaciente/ping')
                    requests.get('http://localhost:4900/monitor/registropaciente')
                    requests.get('http://localhost:4902/registropaciente/ping')
                    requests.get('http://localhost:4900/monitor/registropaciente')                    
                    requests.get('http://localhost:4903/registropaciente/ping')
                except:
                    print('Error en la ejecición')
            print('Experimento Finalizado')
        exito = "Experimento completado"
        inicio = datetime.now()
        fin = datetime.now() + timedelta(seconds=180)
        print('Inicio Experimento', inicio)
        verify(inicio,fin)
        print('Fin Experimento', fin)
        return exito