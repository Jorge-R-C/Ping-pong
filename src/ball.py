import pygame
import random
from settings import ANCHO , ALTURA  

# Pelota
COLOR_PELOTA = (40, 120, 40)
TAM_PELOTA = 15



def crear_pelota():
    pelota = pygame.Rect(ANCHO//2 - TAM_PELOTA//2, ALTURA//2 - TAM_PELOTA, TAM_PELOTA, TAM_PELOTA)
    vel_pelota = [random.choice([-5, 5]), random.choice([-5, 5])]
    return pelota, vel_pelota

def mover_pelota(pelota, vel_pelota):
    pelota.x += vel_pelota[0]
    pelota.y += vel_pelota[1]

    if pelota.top <= 0 or pelota.bottom >=ALTURA:
        vel_pelota[1]*=-1