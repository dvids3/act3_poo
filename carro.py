class carro:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

carro1 = carro("30km/h", "10000km")
print(carro1.kilometraje, carro1.velocidad_maxima)