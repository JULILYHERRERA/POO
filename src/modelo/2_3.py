class Punto_plano_cartesiano:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y}) "

    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return math.sqrt(dx**2 + dy**2)

    def mostrar(self):
        print("coordenadas",self.x,self.y)

    def mover(self, nx, ny):
        self.x= nx
        self.y= ny

distancia_entre_puntos = punto1.calcular_distancia(punto2)
print(f'Distancia {distancia_entre_puntos}')


    


