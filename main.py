import Rectangulo
import Circulo
import pygame, sys
from parametros import *
from random import randint

rec_izd = Rectangulo.Rectangulo([20, ALTO_PANTALLA // 2 - ALTO_BARRA // 2], ANCHO_BARRA,
                                ALTO_BARRA, [0, VELOCIDAD_BARRA])

rec_dch = Rectangulo.Rectangulo([ANCHO_PANTALLA - ANCHO_BARRA - V_MAX, 
ALTO_PANTALLA // 2 - ALTO_BARRA // 2],ANCHO_BARRA, ALTO_BARRA,[0, VELOCIDAD_BARRA])

v_x = randint(V_MIN, V_MAX)
v_y = randint(V_MIN, V_MAX)

while v_x == 0:
    v_x = randint(V_MIN, V_MAX)

pelota = Circulo.Circulo([ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2], RADIO_PELOTA, [v_x, v_y])

puntos_P1 = 0
puntos_P2 = 0

errores = pygame.init()

if(errores[1] > 0):
    print("Error " + errores[1])
else:
    print("Se ha iniciado sin errores")
    
pygame.display.set_caption("Pong")
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

control_fps = pygame.time.Clock()

def pintarRectangulo(rec):
    pygame.draw.rect(pantalla, BLANCO, pygame.Rect(rec.pos[0], rec.pos[1], 
                    rec.ancho,rec.alto))
def pintarCirculo(cir):
    pygame.draw.circle(pantalla, BLANCO, cir.pos, cir.radio)

def teclasP1(teclas):
    direction = ' '
    if teclas[pygame.K_UP]:
        direction = 'UP'
    elif teclas[pygame.K_DOWN]:
        direction = 'DOWN'
    elif teclas[pygame.K_LEFT]:
        direction = 'LEFT'
    elif teclas[pygame.K_RIGHT]:
        direction = 'RIGHT'
    return direction

def teclasP2(teclas):
    direction = ' '
    if teclas[pygame.K_w]:
        direction = 'UP'
    elif teclas[pygame.K_s]:
        direction = 'DOWN'
    elif teclas[pygame.K_d]:
        direction = 'RIGHT'
    elif teclas[pygame.K_a]:
        direction = 'LEFT'
    return direction


def reset(r_izd, r_dch, cir):
    r_izd.pos[1] = ALTO_PANTALLA // 2 - ALTO_BARRA
    r_dch.pos[1] = ALTO_PANTALLA // 2 - ALTO_BARRA

    v_x = randint(V_MIN, V_MAX)
    v_y = randint(V_MIN, V_MAX)

    while v_x == 0:
        v_x = randint(V_MIN, V_MAX)

    cir.pos[0] = ANCHO_PANTALLA // 2
    cir.pos[1] = ALTO_PANTALLA // 2
    cir.velocidad[0] = v_x
    cir.velocidad[1] = v_y

def mostrarPuntos(p1, p2,fuente, color, tam):
    fuente = pygame.font.SysFont(fuente, tam)
    superficie = fuente.render(str(p1) + ' - ' + str(p2), True, color)
    rectangulo = superficie.get_rect()

    rectangulo.midtop = [ANCHO_PANTALLA // 2 , tam]
    
    pantalla.blit(superficie, rectangulo)

def mostrarTexto(txt, fuente_, color, tam):
    fuente = pygame.font.SysFont(fuente_, tam)
    texto = fuente.render(txt, True, color)
    rectangulo = texto.get_rect()
    rectangulo.center = (ANCHO_PANTALLA // 2 - tam , ALTO_PANTALLA // 2 - tam)
    pantalla.blit(texto, rectangulo)

while True:
    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    if puntos_P1 < PUNTOS_MAXIMOS and puntos_P2 < PUNTOS_MAXIMOS:
            
        teclas = pygame.key.get_pressed()
        direction = teclasP1(teclas)
        direction2 = teclasP2(teclas)

        rec_izd.MoverFlechas(direction2, ANCHO_PANTALLA, ALTO_PANTALLA)
        rec_dch.MoverFlechas(direction, ANCHO_PANTALLA, ALTO_PANTALLA)

        pelota.RebotaBordes(ANCHO_PANTALLA, ALTO_PANTALLA)
        pelota.Mover()
        pelota.Colision(rec_dch)
        pelota.Colision(rec_izd)
        
        
        if pelota.pos[0] > rec_dch.pos[0] + ANCHO_BARRA:
            reset(rec_izd, rec_dch, pelota)
            puntos_P1 += 1
            pygame.time.wait(T_ESPERA)
        elif pelota.pos[0] < rec_izd.pos[0]:
            reset(rec_izd, rec_dch, pelota)
            puntos_P2 += 1
            pygame.time.wait(T_ESPERA)
        
    #graficos
    pantalla.fill(NEGRO)
    pintarRectangulo(rec_dch)
    pintarRectangulo(rec_izd)
    pintarCirculo(pelota)
    
    mostrarPuntos(puntos_P1, puntos_P2, FUENTE_MARCADOR, BLANCO, 30)

    if puntos_P1 >= PUNTOS_MAXIMOS:
        mostrarTexto('JUGADOR IZD ha ganado', FUENTE_MSJ, BLANCO , 40)
    elif puntos_P2 >= PUNTOS_MAXIMOS:
        mostrarTexto('JUGADOR DCH ha ganado', FUENTE_MSJ, BLANCO , 40)

    pygame.display.update()
    control_fps.tick(FPS)