import pygame
from settings import ANCHO , ALTURA , FUENTES , RELOJ 
from entities import crear_paletas ,crear_pelota , mover_paletas , mover_pelota
from game import rebotes, quien_anota ,punto_jugador_izq ,punto_jugador_der ,ganador,bot_automatico
from utils import dibujar_elementos , marcador_puntajes

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("Data/musica/Chiptronical.ogg")
pygame.mixer.music.play(-1)

def main():
    pantalla = pygame.display.set_mode((ANCHO, ALTURA))
    pygame.display.set_caption('PING - PONG')

    paleta_izq, paleta_der, vel_paleta = crear_paletas()
    pelota, vel_pelota = crear_pelota()

    punto_izq, punto_der = 0, 0
    pelota_activa = False
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False
                if evento.key == pygame.K_SPACE and not pelota_activa:
                    pelota_activa = True

        mover_paletas(paleta_izq, paleta_der, vel_paleta)
        bot_automatico(paleta_der, vel_paleta, pelota)

        if pelota_activa:
            mover_pelota(pelota, vel_pelota)

        rebotes(pelota, vel_pelota, paleta_izq, paleta_der)

        anota = quien_anota(pelota)
        if anota == "izq":
            punto_izq += punto_jugador_izq(pelota, vel_pelota)
            pelota_activa = False
        if anota == "der":
            punto_der += punto_jugador_der(pelota, vel_pelota)
            pelota_activa = False

        if ganador(punto_izq, punto_der, pantalla):
            ejecutando = False

        dibujar_elementos(pantalla, paleta_izq, paleta_der, pelota)
        marcador_puntajes(pantalla, FUENTES, punto_izq, punto_der)

        pygame.display.flip()
        RELOJ.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()