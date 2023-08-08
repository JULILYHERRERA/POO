class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class circulo:
    def __init__(self, centro, radio):
        self.radio= radio
        self.centro= centro

    def calcular_área(self):
        return math.pi * self.radio **2     

    def calcular_perímetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia= math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia <= self.radio
    

print(f"area {circulo.calcular_área()}")
print(f"perimetro {circulo.calcular_perímetro}")

if circulo.punto_pertenece(punto1):
    print('El punto 1 si pertenece')
else:
    print('El punto 1 no pertenece ')

if circulo.punto_pertenece(punto2):
    print('El punto 2 pertenece ')
else:
    print('El punto 2 no pertenece')