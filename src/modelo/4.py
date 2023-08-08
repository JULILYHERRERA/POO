class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perímetro(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return 2 * (base + altura)

    def calcular_área(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base == altura

# Ejemplo de uso
esquina_sup_izq = Punto(1, 4)
esquina_inf_der = Punto(6, 1)
rectangulo = Rectángulo(esquina_sup_izq, esquina_inf_der)

print(f'Perímetro del rectángulo: {rectangulo.calcular_perímetro()}')
print(f'Área del rectángulo: {rectangulo.calcular_área()}')
print(f'¿El rectángulo es un cuadrado?: {rectangulo.es_cuadrado()}')