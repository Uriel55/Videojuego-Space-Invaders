# Videojuego Space Invaders 

Este es un sencillo clon del célebre videojuego retro conocido como "Space invaders" o "Invasores espaciales", 
que consiste en mover una nave espacial de un lado a otro disparando proyectiles contra una flota de naves extraterrestres que avanzan desde el extremo superior de la pantalla hasta abajo, 
para evitar que lleguen al jugador. 

Está programado con la librería pygame.  
Usa un sistema muy simple de detección de colisiones entre los elementos de la pantalla para determinar la distancia entre el proyectil y los enemigos 
y programar los aciertos del jugador al atinarle a los enemigos, 
así como detectar cuando un enemigo se ha acercado lo suficiente para determinar que el jugador ha perdido. 

El jugador es representado por una imagen de una nave, y la posición y movimiento de la nave se controla mediante las coordenadas de la misma 
Del mismo modo los enemigos son representados por una lista de imágenes de naves extraterrestres, y lo mismo para los proyectiles del jugador. 
También a lo largo del juego se lleva un seguimiento del puntaje del jugador que aumenta eliminando enemigos y que se muestra en la pantalla, durante el juego y después de terminar al perder 

También cuenta con la aparición den "Jefes" enemigos, que intentaran eliminar al jugador disparando sus propios ataques. 
Tanto el jugador como los Jefes enemigos cuentan con un sistema de vida, que disminuye al recibir un disparo o ataque. 
En el caso del jugador, perderá el juego si deja que su vida llegue al límite mínimo. 
En el caso de los Jefes, desaparecerán luego de derrotarlos al atinarles los suficientes ataques para que su vida llegue al límite mínimo, 
al derrotar a un jefe, el jugador recibe un bonus de 30 puntos extra para su puntaje, 
y podrá seguir acumulando puntos eliminando enemigos comunes hasta que aparezca el siguiente Jefe 
