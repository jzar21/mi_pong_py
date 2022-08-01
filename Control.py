import pygame

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