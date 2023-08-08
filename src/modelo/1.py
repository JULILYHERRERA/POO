class vehiculo: 
    def __init__(self, velocidad_max, kilometraje):
        self.velocidad_max= velocidad_max
        self.kilometraje= kilometraje

    def __str__(self):
        return f"la velocidad máxima es {self.velocidad_max} km por hora y su kilometraje es : {self.kilometraje}"    