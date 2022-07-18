from parametros import ACELERACION

class Circulo:
    def __init__(self, pos, radio, velocidad):
        self.pos = pos
        self.radio = radio
        self.velocidad = velocidad

    def Mover(self):
        self.pos[0] += self.velocidad[0]
        self.pos[1] += self.velocidad[1]
        self.velocidad[0] *= ACELERACION
    
    def RebotaBordes(self, ancho, alto):
        if self.pos[1] > (alto - self.radio) or self.pos[1] < (self.radio):
            self.velocidad[1] *= -1
        if self.pos[0] > (ancho - self.radio) or self.pos[0] < (self.radio):
            self.velocidad[0] *= -1
    
    def Colision(self, rectangulo):
        esta_entre_x = self.pos[0] >= rectangulo.pos[0] and self.pos[0] < ( rectangulo.pos[0] + rectangulo.ancho)
        esta_entre_y = self.pos[1] >= rectangulo.pos[1] and self.pos[1] < ( rectangulo.pos[1] + rectangulo.alto)

        if esta_entre_x and esta_entre_y:
            self.velocidad[0] *= -1
            #diferencia normalizada [-1 , 1]
            diferencia = ((-rectangulo.pos[1] - rectangulo.alto / 2 + self.pos[1]) 
                        / (rectangulo.alto / 2 ))
            self.velocidad[1] = diferencia * abs(self.velocidad[0])