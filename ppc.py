class ppc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self, x, y):
        print("las coordenadas son", self.x,"en x",self,y,"en y")
    
    def mover(self, m_x,m_y):
        self.x = m_x
        self.y = m_y
        print("se movio el punto x a", m_x, "se movio el punto y a", m_y)

    def calcular_distacia(self, ppc2):
        dx = ppc2.x - self.x
        dy = ppc2.y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        return distancia

punto1 = ppc(2, 1)
punto1.mostrar(punto1.x, punto1.y)


punto1 = ppc(4, 2)
punto1.mover(punto1.x, punto1.y)


punto2 = ppc(8, 4)
dis = punto1.calcular_distacia(punto2)
print("distancia entre punto 1",punto1,"y punto 2",punto2, "son", dis)










        