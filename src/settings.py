# settings.py
#Aqui esta colores, tamaños, pantalla, fuentes, reloj.
import pygame

# Pantalla
ANCHO, ALTURA = 1200, 800
COLOR_FONDO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Paletas
COLOR_PALETA = (40, 180, 40)
ANCHO_PALETA, ALTO_PALETA = 15, 90

# Pelota
COLOR_PELOTA = (40, 120, 40)
TAM_PELOTA = 15

# Fuentes
pygame.font.init()
FUENTES = pygame.font.SysFont('Arial', 36)
FUENTE_CARTEL = pygame.font.SysFont('Courier New', 60)

# Reloj
RELOJ = pygame.time.Clock()
FPS = 60
