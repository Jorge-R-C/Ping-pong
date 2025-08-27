import pygame
import random
from settings import ALTURA,ANCHO



# Paletas
COLOR_PALETA = (40,180,40)
ANCHO_PALETA = 15
ALTO_PALETA = 90

paleta_izq = 0
paleta_der = 0

def crear_paletas():
    paleta_izq = pygame.Rect(30,ALTURA // 2 - ALTO_PALETA // 2, ANCHO_PALETA,ALTO_PALETA)
    paleta_der = pygame.Rect(ANCHO - 30 -ANCHO_PALETA , ALTURA // 2 - ALTO_PALETA // 2 , ANCHO_PALETA,ALTO_PALETA)
    vel_paleta = 6
    return paleta_izq , paleta_der,vel_paleta


#Movimientos de paleta

def mover_paletas(teclas,paleta_izq,paleta_der,vel_paleta):
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]: paleta_izq.y -= vel_paleta
    if teclas[pygame.K_s]: paleta_izq.y += vel_paleta
    if teclas[pygame.K_UP]: paleta_der.y -= vel_paleta
    if teclas[pygame.K_DOWN]: paleta_der.y += vel_paleta

    #limites para las paletas

    paleta_izq.y = max(0, min(ALTURA - ALTO_PALETA, paleta_izq.y))
    paleta_der.y = max(0,min(ALTURA - ALTO_PALETA,paleta_der.y))
