class Rectangulo:
    def __init__(self, pos, ancho, alto, velocidad):
        self.pos = pos
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad

    def MoverFlechas(self, direccion):
        if direccion == "UP":
            self.pos[1] -= self.velocidad[1]
        elif direccion == "DOWN":
            self.pos[1] += self.velocidad[1]
        elif direccion == "LEFT":
            self.pos[0] -= self.velocidad[0]
        elif direccion == "RIGHT":
            self.pos[0] += self.velocidad[0]
