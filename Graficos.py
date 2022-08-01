import Rectangulo
import Circulo
import pygame, sys
from parametros import *

def mostrarPuntos(pantalla, p1, p2,fuente, color, tam):
    fuente = pygame.font.SysFont(fuente, tam)
    superficie = fuente.render(str(p1) + ' - ' + str(p2), True, color)
    rectangulo = superficie.get_rect()

    rectangulo.midtop = [ANCHO_PANTALLA // 2 , tam]
    
    pantalla.blit(superficie, rectangulo)

def mostrarTexto(pantalla ,txt, fuente_, color, tam):
    fuente = pygame.font.SysFont(fuente_, tam)
    texto = fuente.render(txt, True, color)
    rectangulo = texto.get_rect()
    rectangulo.center = (ANCHO_PANTALLA // 2 - tam , ALTO_PANTALLA // 2 - tam)
    pantalla.blit(texto, rectangulo)

def pintarRectangulo(pantalla, rec):
    pygame.draw.rect(pantalla, BLANCO, pygame.Rect(rec.pos[0], rec.pos[1], 
                    rec.ancho,rec.alto))
def pintarCirculo(pantalla, cir):
    pygame.draw.circle(pantalla, BLANCO, cir.pos, cir.radio)

def mostrarFps(pantalla, fps):
    fuente = pygame.font.SysFont('consolas', 20)
    texto = fuente.render(str(int(fps)) + ' FPS', True, BLANCO)
    rectangulo = texto.get_rect()
    rectangulo.topleft = (10, 10)
    pantalla.blit(texto, rectangulo)