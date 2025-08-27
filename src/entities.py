#Aqui estan las funciones de movmiento de paletas y pelota
import pygame
import random
from settings import ANCHO , ALTURA , ANCHO_PALETA , ALTO_PALETA ,TAM_PELOTA

def crear_paletas():
    paleta_izq = pygame.Rect(30, ALTURA//2 - ALTO_PALETA//2, ANCHO_PALETA, ALTO_PALETA)
    paleta_der = pygame.Rect(ANCHO - 30 - ANCHO_PALETA, ALTURA//2 - ALTO_PALETA//2, ANCHO_PALETA, ALTO_PALETA)
    vel_paleta = 6
    return paleta_izq, paleta_der, vel_paleta

def crear_pelota():
    pelota = pygame.Rect(ANCHO//2 - TAM_PELOTA//2, ALTURA//2 - TAM_PELOTA, TAM_PELOTA, TAM_PELOTA)
    vel_pelota = [random.choice([-5, 5]), random.choice([-5, 5])]
    return pelota, vel_pelota

def mover_paletas(paleta_izq, paleta_der, vel_paleta):
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]: paleta_izq.y -= vel_paleta
    if teclas[pygame.K_s]: paleta_izq.y += vel_paleta
    if teclas[pygame.K_UP]: paleta_der.y -= vel_paleta
    if teclas[pygame.K_DOWN]: paleta_der.y += vel_paleta

    paleta_izq.y = max(0, min(ALTURA - ALTO_PALETA, paleta_izq.y))
    paleta_der.y = max(0, min(ALTURA - ALTO_PALETA, paleta_der.y))

def mover_pelota(pelota, vel_pelota):
    pelota.x += vel_pelota[0]
    pelota.y += vel_pelota[1]

    if pelota.top <=0 or pelota.bottom >= ALTURA:
        vel_pelota [1] *= -1
