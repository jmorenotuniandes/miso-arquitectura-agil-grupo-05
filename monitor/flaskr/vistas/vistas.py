from typing import Any
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import time
from random import randrange
import logging
import sys
import requests
import signal
import sys
from threading import Thread
from datetime import datetime, timedelta

class Llamadas():

    def llamarMicroservicio1(e, microservicio): 

        fallo1 = None
        fallo2 = None    
        fallo3 = None

        loggerName = 'MonitorMicroservicio1'
        urlMicroservicio = 'https://microservicio-uno-grupo5.herokuapp.com/registropaciente/ping'
        if(microservicio == 2): 
            loggerName = 'MonitorMicroservicio2'
            urlMicroservicio = 'https://microservicio-dos-grupo5.herokuapp.com/registropaciente/ping'
        else:
            if(microservicio == 3):
                loggerName = 'MonitorMicroservicio3'
                urlMicroservicio = 'https://microservicio-tres-grupo5.herokuapp.com/registropaciente/ping'
            
        # create logger
        logger = logging.getLogger(loggerName)
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


        inicio = datetime.now()
        fin = datetime.now() + timedelta(seconds=180)
        while fin > datetime.now():
            fallo = None
            try:
                r = requests.get(urlMicroservicio, timeout=10)
                if(r.status_code != 200):
                    logger.debug('Error en microservicio #' + str(microservicio) + ' Código respuesta: '+ str(r.status_code)  )
                    fallo = datetime.now()                        
            except:
                logger.debug('Error en microservicio #' + str(microservicio) + ': timeout' )
                fallo = datetime.now()
            if(fallo != None):
                limiteInferior = fallo - timedelta(seconds=20)
                limiteSuperior = fallo
                fallosEnRango = 1
                if(fallo1 == None):
                    fallo1 = fallo
                    fallo = None
                else:
                    if(fallo1 < limiteInferior or fallo1 > limiteSuperior):
                        fallo1 = fallo
                        fallo = None
                    else:
                        fallosEnRango = fallosEnRango + 1
                if(fallo2 == None):
                    fallo2 = fallo
                    fallo = None
                else:
                    if(fallo2 < limiteInferior or fallo2 > limiteSuperior):
                        fallo = fallo
                        fallo = None
                    else:
                        fallosEnRango = fallosEnRango + 1
                if(fallo3 == None):
                    fallo3 = fallo
                    fallo = None
                else:
                    if(fallo3 < limiteInferior or fallo3 > limiteSuperior):
                        fallo3 = fallo
                        fallo = None
                    else:
                        fallosEnRango = fallosEnRango + 1
                if(fallosEnRango == 3):
                    logger.debug('Microservicio #' + str(microservicio) + ' en estado de fallo. Rango errores entre ' + str(limiteInferior) + ' y ' + str(limiteSuperior))
                    fallo1 = None
                    fallo2 = None
                    fallo3 = None
                    fallosEnRango = 0
            time.sleep(1)
        logger.removeHandler(ch)

class VistaMonitorRegistroPaciente(Resource):

    def get(self):

        call = Llamadas()

        threads = []
        # create the threads
        t1 = Thread(target=call.llamarMicroservicio1, args=(1,))
        t2 = Thread(target=call.llamarMicroservicio1, args=(2,))
        t3 = Thread(target=call.llamarMicroservicio1, args=(3,))
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        t1.start()
        t2.start()
        t3.start()

        # wait for the threads to finish
        [ t.join() for t in threads ]

        return 'OK', 200