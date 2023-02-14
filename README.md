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


![Captura de pantalla_20230214_033655](https://user-images.githubusercontent.com/101745244/218871877-531803e0-7725-4653-9e0e-434cdb5e0bd4.png)
![Captura de pantalla_20230214_034923](https://user-images.githubusercontent.com/101745244/218871944-9d921a32-2038-45db-9b65-686ec63f89cf.png)
![Captura de pantalla_20230214_035010](https://user-images.githubusercontent.com/101745244/218871954-2da11105-6df7-4039-b2c5-6186f2c2a6ad.png)
![Captura de pantalla_20230214_035047](https://user-images.githubusercontent.com/101745244/218872400-26b0fbe9-ba9f-48ae-b81a-6827524a58f4.png)
![Captura de pantalla_20230214_035115](https://user-images.githubusercontent.com/101745244/218872429-6ffc0af8-314b-4c81-a5e2-68473262d247.png)
![Captura de pantalla_20230214_033736](https://user-images.githubusercontent.com/101745244/218872492-63b7acaf-7b16-4613-a1d3-aba5b0324932.png)
![Captura de pantalla_20230214_034418](https://user-images.githubusercontent.com/101745244/218872507-8f8eb6da-72e4-4714-857b-61d985361951.png)
![Captura de pantalla_20230214_034656](https://user-images.githubusercontent.com/101745244/218872522-7421ef1f-8e2b-4047-85de-6ac665509667.png)
![Captura de pantalla_20230214_034724](https://user-images.githubusercontent.com/101745244/218872693-a14f1831-52f7-4511-a16c-0d89ef2eccbe.png)
![Captura de pantalla_20230214_034227](https://user-images.githubusercontent.com/101745244/218872774-ad7fef1d-0e46-419d-9edf-4b2283696cb7.png)
