from Circulo import *
from parametros import *
from Rectangulo import *
from random import randint
from Control import *
from Graficos import *
import pygame

class Game:
    def __init__(self):
        self.rec_izd = Rectangulo.Rectangulo([20, ALTO_PANTALLA // 2 - ALTO_BARRA // 2], ANCHO_BARRA,ALTO_BARRA, [0, VELOCIDAD_BARRA])

        self.rec_dch = Rectangulo.Rectangulo([ANCHO_PANTALLA - ANCHO_BARRA - V_MAX, ALTO_PANTALLA // 2 - ALTO_BARRA // 2], ANCHO_BARRA, ALTO_BARRA,[0, VELOCIDAD_BARRA])

        v_x = randint(V_MIN, V_MAX)
        v_y = randint(V_MIN, V_MAX)
        self.pelota = Circulo.Circulo([ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2], RADIO_PELOTA, [v_x, v_y])

        self.puntos_P1 = 0
        self.puntos_P2 = 0

    def __reset(self):
        self.rec_izd.pos[1] = ALTO_PANTALLA // 2 - ALTO_BARRA
        self.rec_dch.pos[1] = ALTO_PANTALLA // 2 - ALTO_BARRA

        v_x = randint(V_MIN, V_MAX)
        v_y = randint(V_MIN, V_MAX)

        while v_x == 0:
            v_x = randint(V_MIN, V_MAX)

        self.pelota.pos[0] = ANCHO_PANTALLA // 2
        self.pelota.pos[1] = ALTO_PANTALLA // 2
        self.pelota.velocidad[0] = v_x
        self.pelota.velocidad[1] = v_y

    def Actualizar(self, pantalla):
        if self.puntos_P1 < PUNTOS_MAXIMOS and self.puntos_P2 < PUNTOS_MAXIMOS:
            
            teclas = pygame.key.get_pressed()
            direction = teclasP1(teclas)
            direction2 = teclasP2(teclas)

            self.rec_dch.MoverFlechas(direction, ANCHO_PANTALLA, ALTO_PANTALLA)
            self.rec_izd.MoverFlechas(direction2, ANCHO_PANTALLA, ALTO_PANTALLA)

            self.pelota.RebotaBordes(ANCHO_PANTALLA, ALTO_PANTALLA)
            self.pelota.Mover()
            self.pelota.Colision(self.rec_dch)
            self.pelota.Colision(self.rec_izd)
            
            
            if self.pelota.pos[0] > self.rec_dch.pos[0] + ANCHO_BARRA:
                self.__reset()
                self.puntos_P1 += 1
                pygame.time.wait(T_ESPERA)
            elif self.pelota.pos[0] < self.rec_izd.pos[0]:
                self.__reset()
                self.puntos_P2 += 1
                pygame.time.wait(T_ESPERA)

        pantalla.fill(NEGRO)
        pintarRectangulo(pantalla, self.rec_dch)
        pintarRectangulo(pantalla, self.rec_izd)
        pintarCirculo(pantalla, self.pelota)
        
        mostrarPuntos(pantalla, self.puntos_P1, self.puntos_P2, FUENTE_MARCADOR, BLANCO, 30)

        if self.puntos_P1 >= PUNTOS_MAXIMOS:
            mostrarTexto(pantalla, 'JUGADOR IZD ha ganado', FUENTE_MSJ, BLANCO , 40)
        elif self.puntos_P2 >= PUNTOS_MAXIMOS:
            mostrarTexto(pantalla, 'JUGADOR DCH ha ganado', FUENTE_MSJ, BLANCO , 40)