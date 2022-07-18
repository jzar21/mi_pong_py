class Rectangulo:
    def __init__(self, pos, ancho, alto, velocidad):
        self.pos = pos
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad

    def MoverFlechas(self, direccion, ancho, alto):
        if direccion == "UP":
            self.pos[1] -= self.velocidad[1]
        elif direccion == "DOWN":
            self.pos[1] += self.velocidad[1]
        elif direccion == "LEFT":
            self.pos[0] -= self.velocidad[0]
        elif direccion == "RIGHT":
            self.pos[0] += self.velocidad[0]

        self.__AjustarPos(ancho, alto)

    def __AjustarPos(self, ancho, alto):
        if self.pos[1] < 0:
            self.pos[1] = 0

        elif self.pos[1] > alto - self.alto:
            self.pos[1] = alto - self.alto

        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] > ancho - self.ancho:
            self.pos[0] = ancho - self.ancho