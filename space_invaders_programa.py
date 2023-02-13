import pygame
import random
import math
from pygame import mixer

# Velocidades para los diferentes elementos del juego
VELOCIDAD_ENEMIGO = 0.6
VELOCIDAD_PROYECTIL = 0.9
VELOCIDAD_JEFE = 0.2
VELOCIDAD_JEFE_DAÑADO = 0.01
VELOCIDAD_ATAQUE_ENEMIGO = 0.9
VELOCIDAD_JUGADOR = 0.8

# Inicializar pygame
pygame.init()

# Crear la pantalla o ventana
pantalla = pygame.display.set_mode((800,600))

# Fondo
fondo = pygame.image.load('imgs/espacio3.jpg')
fondo = pygame.transform.scale(fondo, (800, 600))

# Sonidos
mixer.music.load('music/musica_fondo.wav')
mixer.music.play(-1)

# Titulo e Icono
pygame.display.set_caption("Invasores Espaciales Por Uriel55")
icono = pygame.image.load('imgs/ovni9.png')
pygame.display.set_icon(icono)

# Jugador, configuraciones
jugadorNombre = "Jugador 1"
fuente_jugador = pygame.font.Font("fuentes/arcadefont2.TTF", 15)

jugadorImg = pygame.image.load('imgs/sp_sh8.png')
jugadorImg = pygame.transform.scale(jugadorImg, (66, 66)) 
jugadorX = 370
jugadorY = 525   
jugadorX_cambio = 0

jugadorDañado = pygame.image.load('imgs/sp_sh8_dañada.png')
jugadorDañado = pygame.transform.scale(jugadorDañado, (66, 66))

jugadorIcon = pygame.transform.scale(jugadorImg, (32, 32))

# Configuraciones para jefes
num_jefes = 5
jefeTurno = 0
jefeImg = []

# Aspecto de los jefes
for i in range(num_jefes):
    jefeImg.append(pygame.image.load(f'imgs/jefe{i+1}.png'))
    jefeImg[i] = pygame.transform.scale(jefeImg[i], (100, 100))

# Aspecto de los jefes bajo daño
jefeDañado = []
for i in range(num_jefes):
    jefeDañado.append(pygame.image.load(f'imgs/jefe{i+1}daño.png'))
    jefeDañado[i] = pygame.transform.scale(jefeDañado[i], (100, 100))

# Nombres de los jefes
villanoNombre = ["El Devorador Cósmico","El Portador Del Vacío","La Peste Galáctica","El Ejecutor Supremo","La Semilla Estelar"]

# Aspecto de los ataques de los enemigos
ataqueEnemigoImg = []
for i in range(num_jefes):
    ataqueEnemigoImg.append(pygame.image.load(f'imgs/blast{i+1}.png'))
    ataqueEnemigoImg[i] = pygame.transform.scale(ataqueEnemigoImg[i], (85,85))

# Configuración para el movimiento de los jefes
jefeX = 350
jefeY = 10
jefeX_cambio = VELOCIDAD_JEFE
jefeX_cambio_bajo_daño = VELOCIDAD_JEFE_DAÑADO


# Fuente para escribir el nombre del jefe
fuente_villano = pygame.font.Font("fuentes/arcadefont2.TTF", 15)


# Enemigos comunes, configuración
enemigoImg = []
enemigoX = []
enemigoY = []
enemigoX_cambio = []
enemigoY_cambio = []
num_enemigos = 6

# Cantidad de enemigos comunes
for i in range(num_enemigos):
    enemigoImg.append(pygame.image.load('imgs/enemigo3.png'))
    enemigoImg[i] = pygame.transform.scale(enemigoImg[i], (64, 64))
    enemigoX.append(random.randint(1,735))
    enemigoY.append(random.randint(50,150))
    enemigoX_cambio.append(VELOCIDAD_ENEMIGO)
    enemigoY_cambio.append(40)

# Disparo del jugador
proyectilImg = pygame.image.load('imgs/bullet.png')
proyectilImg = pygame.transform.scale(proyectilImg, (64, 64))
proyectilY_inicio = 475
proyectilX = 0
proyectilY = proyectilY_inicio
proyectilX_cambio = 0
proyectilY_cambio = VELOCIDAD_PROYECTIL
proyectil_estado = "listo"


# Disparos de los jefes
ataqueEnemigoY_inicio = 20
ataqueEnemigoY = ataqueEnemigoY_inicio
ataqueEnemigoY_cambio = VELOCIDAD_ATAQUE_ENEMIGO
ataqueEnemigoX = 0
ataqueEnemigoX_cambio = 0
ataqueEnemigo_estado = "listo"
ataqueEnemigo_coordenada = random.randint(2,705)

# Puntaje del jugador
valor_puntaje = 0
fuente = pygame.font.Font("fuentes/arcadefont2.TTF", 32)
puntos_nivel = 0

textoX = 10
textoY = 10

# Texto Game Over
GO_fuente = pygame.font.Font('fuentes/arcadefont2.TTF', 64)
GAME_OVER = False
BATALLA = False

# Dibujar jefe
def jefe_boss(Img,x,y): 
    pantalla.blit(Img, (x,y))

# Escribir el texto de game over
def texto_game_over():
    GO_texto = GO_fuente.render("GAME OVER", True, (255,255,255))
    pantalla.blit(GO_texto, (200,250))

# Escribir puntaje del jugador
def mostrar_puntaje(x,y):
    puntaje = fuente.render("PUNTAJE : " + str(valor_puntaje), True, (255,255,255))
    pantalla.blit(puntaje, (x,y))
    
# Escribir el nombre del jugador
def mostrar_jugador_nombre(x,y):
    nombre = fuente_jugador.render(f"{jugadorNombre}", True, (0,255,0))
    pantalla.blit(nombre, (x,y))

# Escribir el nombre del jefe
def mostrar_villano_nombre(x,y):
    nombre = fuente_villano.render(f"{villanoNombre[jefeTurno]}", True, (255,0,0))
    pantalla.blit(nombre, (x,y))
    
    puntaje_plus = fuente_villano.render("+30 Puntos", True, (255,0,0))
    pantalla.blit(puntaje_plus, (x,y+40))

# Dibujar al jugador
def jugador(Img,x,y):
    pantalla.blit(Img, (x,y))

# Dibujar enemigo comun
def enemigo(x,y,i):
    pantalla.blit(enemigoImg[i], (x,y))

# Dibujar disparos del Jugador
def disparar(x,y):
    global proyectil_estado
    proyectil_estado = "fuego"
    pantalla.blit(proyectilImg, (x+1,y+10))

# Dibujar disparos del jefe
def ataques_enemigos(x,y):
    global ataqueEnemigo_estado
    ataqueEnemigo_estado = "fuego"
    pantalla.blit(ataqueEnemigoImg[jefeTurno], (x+1,y+10))

# Comprobar colisiones de proyectiles y objetivos
def esColision(enemigoX,enemigoY, proyectilX,proyectilY,enemigoTipo):
    extencionX = 0
    if enemigoTipo == 'comun':
        extencionX = 5
    elif enemigoTipo == 'jefe':
        extencionX = 20
    elif enemigoTipo == 'jugador':
        extencionX = -23
    distancia = math.sqrt((math.pow((enemigoX+extencionX)-(proyectilX), 2)) + (math.pow((enemigoY+5)-(proyectilY+5), 2)))
    if distancia > 25 and distancia < 36:
        return True
    else:
        return False

# Declaración de variables
bonus = False  

tiempo_daño = None # Mostrar jugador con aspecto "dañado"
tiempo_limite = 800

derecha = True
izquierda = False

daño_jugador = False
# Vida del jugador
vida_jugadorXInit = 15
vida_jugadorXTam = 100

# Vida del jefe
vida_jefeXTam=300
vida_jefeXIni = 485

daño_jefe = False  # Mostrar jefe con aspecto "dañado"
coordenada = 0  # Coordenadas que el jefe recorre estando dañado

# Correr juego
corriendo = True

# Bucle del juego
while corriendo:
    
    pantalla.fill((2, 20, 48))  # RGB
    
    # Imagen Fondo
    pantalla.blit(fondo,(0,0))
        
             
            
    # Eventos de pygame para el juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            
        if evento.type == pygame.KEYDOWN:
            # Mover jugador a la izquierda
            if evento.key == pygame.K_LEFT:   
                jugadorX_cambio = -VELOCIDAD_JUGADOR
            # Mover jugador a la derecha
            if evento.key == pygame.K_RIGHT:
                jugadorX_cambio = VELOCIDAD_JUGADOR
                
            # Disparar proyectiles del jugador
            if evento.key == pygame.K_SPACE:
                if GAME_OVER!=True:
                    if proyectil_estado == "listo":
                        proyectil_sonido = mixer.Sound('music/laser.wav')
                        proyectil_sonido.play()
                        # Usar la coordenada x de la nave para dársela al proyectil
                        proyectilX = jugadorX 
                        disparar(proyectilX,proyectilY)
                    
        # Detener movimiento del jugador 
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 0
           
    # Limites de mapa para el jugador
    if daño_jugador == True:
        jugadorX = jugadorX
    else:
        jugadorX += jugadorX_cambio
    
    if jugadorX <= 1:
        jugadorX = 1
    elif jugadorX >= 735:
        jugadorX = 735
        
        
    # Colisiones Jugador con los ataques enemigos       
    colisionJugador = esColision(jugadorX, jugadorY, ataqueEnemigoX, ataqueEnemigoY, "jugador")
    if colisionJugador:
        
        explocion_sonido = mixer.Sound('music/explocion.wav')
        explocion_sonido.play()
        ataqueEnemigoY = ataqueEnemigoY_inicio
        ataqueEnemigo_estado = "listo"

        # Efecto de daño en el jugador
        daño_jugador = True
        vida_jugadorXTam -= 25
        
        tiempo_daño = pygame.time.get_ticks()

    
    # Dibujar vida del jugador
    if GAME_OVER!=True:
        pygame.draw.rect(pantalla, (0, 255, 0), (10, 495, 110, 20), 2)
        pygame.draw.rect(pantalla, (0, 255, 0), (15, 500, vida_jugadorXTam, 10))
        mostrar_jugador_nombre(10,475)

    # Perder juego si la vida del jugador baja por completo
    if vida_jugadorXTam <= 0:
        GAME_OVER = True
        texto_game_over()
    
    # Tiempo del efecto de daño del jugador
    if tiempo_daño is not None:
        tiempo_pasado = pygame.time.get_ticks() - tiempo_daño
        if tiempo_pasado >= tiempo_limite:
            daño_jugador = False
            event_time = None
            
        
        
    # Movimiento de proyectil del jugador
    # Reincorporar proyectil cuando rebase el límite de la pantalla
    if proyectilY < 0:
        proyectilY = proyectilY_inicio
        proyectil_estado = "listo"
    
    # Mover el proyectil
    if proyectil_estado == "fuego":
        disparar(proyectilX,proyectilY)
        proyectilY -= proyectilY_cambio

            
    # Dibujar al jugador
    if GAME_OVER != True:
        if daño_jugador == False:
            jugador(jugadorImg,jugadorX,jugadorY)
        elif daño_jugador == True:
            jugador(jugadorDañado,jugadorX,jugadorY)
    
        
        
    # Limites de mapa para los enemigos comunes
    for i in range(num_enemigos):
        
        # Game Over. Perder juego cuando un enemigo común se acerque al límite del jugador
        if enemigoY[i] > 415:
            for j in range(num_enemigos):
                enemigoY[j] = 2000
            texto_game_over()
            GAME_OVER = True
            break
        
        # Mover enemigo comun de lado a lado
        enemigoX[i] += enemigoX_cambio[i]
        
        # Limite izquierdo para enemigo común, avanzar hasia abajo y cambiar de dirección
        if enemigoX[i] <= 1:
            enemigoX_cambio[i] = VELOCIDAD_ENEMIGO
            enemigoY[i] += enemigoY_cambio[i]
        
        # Limite derecho para enemigo común, avanzar hasia abajo y cambiar de dirección
        elif enemigoX[i] >= 736:
            enemigoX_cambio[i] = -VELOCIDAD_ENEMIGO
            enemigoY[i] += enemigoY_cambio[i]
            
            
        # Colisiones Enemigos Comunes con el proyectil del jugador
        colision = esColision(enemigoX[i], enemigoY[i], proyectilX, proyectilY, 'comun')
        if colision:
            explocion_sonido = mixer.Sound('music/explocion.wav')
            explocion_sonido.play()
            proyectilY = proyectilY_inicio
            proyectil_estado = "listo"
            valor_puntaje += 1
            
            # Subir puntaje despues de eliminar un enemigo común
            if BATALLA == False:
                puntos_nivel += 1
                
                # Iniciar batalla con el jefe. Despues de 10 enemigos comunes eliminados, iniciar batalla con un jefe
                if puntos_nivel >= 10:
                    BATALLA = True
            
            # Reaparecer enemigo común en un punto aleatorio de la parte superior de la pantalla después de ser eliminado
            enemigoX[i] = random.randint(0,735)
            enemigoY[i] = random.randint(50,150)

        # Dibujar enemigo común (solo si no se ha perdido y terminado el juego)
        if GAME_OVER!=True:
            enemigo(enemigoX[i],enemigoY[i], i)
            
            
            
    # Reiniciar el orden de los jefes
    if jefeTurno >= 5:
        jefeTurno = 0
        
    # Reducir el numero de enemigos comunes durante batalla con jefe
    if BATALLA == True:
        num_enemigos = 4
    
        # Movimiento normal del jefe
        if daño_jefe==False:
            jefeX += jefeX_cambio
        # Movimiento del jefe dañado
        elif daño_jefe==True:
            jefeX += jefeX_cambio_bajo_daño
            
    # Limites de mapa para jefe
        # Limite izquierdo
        if jefeX <= 1:
            jefeX_cambio = VELOCIDAD_JEFE
            jefeX_cambio_bajo_daño = VELOCIDAD_JEFE_DAÑADO
            derecha = True
            izquierda = False
        # Limite derecho
        elif jefeX >= 706:
            jefeX_cambio = -VELOCIDAD_JEFE
            jefeX_cambio_bajo_daño = -VELOCIDAD_JEFE_DAÑADO
            derecha = False
            izquierda = True
            
        # Dibujar el disparo del jefe, al llegar a la coordenada aleatoria en la que se debe disparar
        if jefeX>ataqueEnemigo_coordenada-3 and jefeX<ataqueEnemigo_coordenada+3:
   
            if GAME_OVER!=True:
                # Disparar ataque enemigo
                if ataqueEnemigo_estado == "listo":
                    proyectil_sonido = mixer.Sound('music/laser.wav')
                    proyectil_sonido.play()
                    # Usar la coordenada x de la nave para dársela al proyectil
                    ataqueEnemigoX = jefeX 
                    ataques_enemigos(ataqueEnemigoX, ataqueEnemigoY)
                    ataqueEnemigo_coordenada = random.randint(2,705)
               
        
            
        # Colisiones Jefes
        # Comprobar si el proyectil de jugador ha chocado con el jefe
        colisionJefe = esColision(jefeX, jefeY, proyectilX, proyectilY, 'jefe')
        if colisionJefe:
            explocion_sonido = mixer.Sound('music/explocion.wav')
            explocion_sonido.play()
            proyectilY = proyectilY_inicio
            proyectil_estado = "listo"
        
            
            # Activar efecto de aspecto dañado en el jefe
            daño_jefe = True 
            # Bajar vida del jefe
            vida_jefeXTam -= 20
            vida_jefeXIni += 20
           
            # Movimiento del jefe dañado
            if derecha:
                coordenada = jefeX+25
            if izquierda:
                coordenada = jefeX-25
        
        
        # Dibujar vida de Jefe enemigo
        if GAME_OVER!=True:
            pygame.draw.rect(pantalla, (255, 0, 0), (480, 35, 310, 20), 2)
            pygame.draw.rect(pantalla, (255, 0, 0), (vida_jefeXIni, 40, vida_jefeXTam, 10))  #x=410
            mostrar_villano_nombre(480,15)
        
        # Derrotar al jefe cuando su vida baje al mínimo
        if vida_jefeXTam <= 0:
            BATALLA = False
            valor_puntaje += 30
            puntos_nivel = 0
            vida_jefeXTam = 300
            vida_jefeXIni = 485
            
            jefeTurno += 1
            num_enemigos = 6
                
            
        
        # Movimiento ataques enemigos    
        if ataqueEnemigoY > 600:
            ataqueEnemigoY = ataqueEnemigoY_inicio
            ataqueEnemigo_estado = "listo"
            
        if ataqueEnemigo_estado == "fuego":
            ataques_enemigos(ataqueEnemigoX,ataqueEnemigoY)
            ataqueEnemigoY += ataqueEnemigoY_cambio
            
        # Recuperación de jefe del daño, retomar aspecto y velocidad normal del jefe
        if daño_jefe:
            if derecha:
                if jefeX >= coordenada:
                    daño_jefe = False
    
            elif izquierda:
                if jefeX <= coordenada:
                    daño_jefe = False
    
        # Dibujar jefe
        if GAME_OVER!=True:
            # Aspeto normal
            if daño_jefe == False:
                jefe_boss(jefeImg[jefeTurno],jefeX,jefeY)
            # Aspecto dañado
            elif daño_jefe == True:
                jefe_boss(jefeDañado[jefeTurno],jefeX,jefeY)
                
    # Mostrar el puntaje del jugador
    mostrar_puntaje(textoX,textoY)
    
    
    # Línea que marca el límite de avance de los enemigos
    pygame.draw.line(pantalla, (255,255,255), (0,470), (800,470), 9)
    
    pygame.display.update()