# Aqui estan las funines de rebotes,punto,ganador y bot 
import pygame
import random
from settings import ALTURA , ANCHO , ALTO_PALETA , FUENTE_CARTEL , COLOR_FONDO


rebote = 0

def punto_jugador_izq(pelota, vel_pelota):
    global rebote
    pelota.center = (ANCHO // 2, ALTURA // 2)
    vel_pelota[:] = [random.choice([4, -4]), random.choice([4, -4])]
    rebote = 0
    return 1  # retorna el punto ganado

def punto_jugador_der(pelota, vel_pelota):
    global rebote
    pelota.center = (ANCHO // 2, ALTURA // 2)
    vel_pelota[:] = [random.choice([4, -4]), random.choice([4, -4])]
    rebote = 0
    return 1

#Rebotes en paleta 
rebote = 0
def rebotes(pelota,vel_pelota,paleta_izq,paleta_der):
    global rebote
    if pelota.colliderect(paleta_izq) or pelota.colliderect(paleta_der):
        vel_pelota[0] *=-1
        rebote += 1
        if rebote % 4 == 0:
            vel_pelota[0] *= 1.2
            vel_pelota[1] *= 1.2   

def quien_anota(pelota):
    if pelota.left <= 0:
        return "der"
    if pelota.right >= ANCHO:
        return "izq"
    return None

def bot_automatico(paleta_der, vel_paleta, pelota):
    if pelota.centery > paleta_der.centery + random.randint(10, 40):
        paleta_der.y += vel_paleta
    elif pelota.centery < paleta_der.centery + random.randint(10, 40):
        paleta_der.y -= vel_paleta
    paleta_der.y = max(0, min(ALTURA - ALTO_PALETA, paleta_der.y))

def ganador(punto_izq, punto_der, pantalla):
    if punto_izq >= 10 or punto_der >= 10:
        ganador = "IZQUIERDA" if punto_izq >= 10 else "DERECHA"
        texto_ganador = FUENTE_CARTEL.render(f"Ganador {ganador}!!", True, (75, 90, 75))
        pantalla.fill(COLOR_FONDO)
        pantalla.blit(texto_ganador, (ANCHO // 2 - 350, ALTURA // 2 - 25))
        pygame.display.flip()
        pygame.time.delay(2000)
        return True
    return False