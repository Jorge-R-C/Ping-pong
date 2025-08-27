# src/utils.py
#Funciones para dibujar en pantalla 
import pygame
from settings import BLANCO, COLOR_FONDO, COLOR_PALETA, COLOR_PELOTA, ANCHO, ALTURA

def dibujar_elementos(pantalla, paleta_izq, paleta_der, pelota):
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_PALETA, paleta_izq)
    pygame.draw.rect(pantalla, COLOR_PALETA, paleta_der)
    pygame.draw.ellipse(pantalla, COLOR_PELOTA, pelota)
    pygame.draw.aaline(pantalla, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTURA))

def marcador_puntajes(pantalla, fuente, punto_izq, punto_der):
    marcador = fuente.render(f"{punto_izq} : {punto_der}", True, BLANCO)
    pantalla.blit(marcador, (ANCHO // 2 - marcador.get_width() // 2, 20))
