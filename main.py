from parametros import *
import pygame, sys, Game, Graficos, Control

def main():
    mi_juego = Game.Game()
    errores = pygame.init()

    if(errores[1] > 0):
        print("Error " + errores[1])
    else:
        print("Se ha iniciado sin errores")
        
    pygame.display.set_caption("Pong")
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

    control_fps = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        mi_juego.Actualizar(pantalla)
        fps = control_fps.get_fps()
        Graficos.mostrarFps(pantalla, fps)
        control_fps.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()