# miso-arquitectura-agil-grupo-05
Repositorio de documentación para el grupo 05 de arquitecturas ágiles.

# Detalles Microservicio
Tiene un arreglo de codigos de HTML, 0, 200 y varios de errores comunes.
Se genera un número al azar para seleccionar un código de respuesta.
Si el código de respuesta es 0 se genera una espera de 20 segundo para generar un timeout para el monitor.
Los otros códigos se envian como respuesta con un texto
En el log se puede ver algo así: 10/09/2021 03:30:12 PM - LlamadaMicroservicio - DEBUG - 200 OK

# Requerimientos de monitor:

* El monitor debe correr durante 3 minutos.
* Genera una llamada a cada uno de los tres microservicios cada segundo usando el URL de Heroku.
* Cada llamada debe tener un timeout de 10 segundos.

* Debe poner estar generando llamadas para las 3 instancias al mismo tiempo, esto significa que son hilos para cada llamada que generen un evento al hilo principal cuando terminen la ejecución
* Si el microservicio devuelve un código que no es 200 o da un timeout, eso se considera un fallo.
* Cada vez que ocurra un fallo debe identificar si en los ultimos 20 segundos (20 segundos, no 20 llamadas) han habido al menos 3 fallos. Para esto debe mantener el estado de las respuestas de cada microservicio
* Debe loguear las respuestas de las llamadas de cada servicio y cuando detecte que un microservicio esté en estado fallido (3 fallos en 20 segundos). Loguear que ese microservicio se encuentra en estado fallido y resetear las llamadas es decir, reiniciar la cuenta de fallos.

# URLs
Microservicio 1: https://microservicio-uno-grupo5.herokuapp.com/registropaciente/ping
Microservicio 2: https://microservicio-dos-grupo5.herokuapp.com/registropaciente/ping
Microservicio 3: https://microservicio-tres-grupo5.herokuapp.com/registropaciente/ping

# Ejecución del experimento

* Hacer llamada al monitor: https://monitor-grupo5.herokuapp.com/monitor/registropaciente
* Sacar los de cada microservicio y el monitor, pasarlos a excel y filtrar solo por las lineas que nos interesan
* Analizar los datos para aceptar o rechazar la hipótesis

