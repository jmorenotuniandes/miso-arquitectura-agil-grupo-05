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
* Genera una llamada a cada uno de los tres microservicios cada segundo
* Debe poner estar generando llamadas para las 3 instancias al mismo tiempo
* debe identificar si en los ultimos 20 segundos (20 segundos, no 20 llamadas) han habido al menos 3 fallos. Para esto debe mantener el estado de las respuestas de cada microservicio
* Debe loguear los resultados que las llamadas de cada servicio y cuando detecte que un microservicio esté en estado fallido. Poner un microservicio en estado fallido reseteala las llamadas, o sea comienza la cuenta de tres fallos de nuevo.
