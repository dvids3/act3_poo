class pr:
    def __init__(self,x , y):
        self.x = x
        self.y = y

class rec:
    def __init__(self, esqder, esqiz):
        self.esqder= esqder
        self.esqiz = esqiz
     
    def calperimetro(self):
        ancho = self.esqder.x - self.esqiz.x
        alto = self.esqder.y - self.esqiz.y
        return 2 * (ancho + alto)
    
    def calarea(self):
        ancho = self.esqder.x - self.esqiz.x
        alto = self.esqder.y - self.esqiz.y
        return ancho * alto
    
    def escua(self):
        ancho = self.esqder.x - self.esqiz.x
        alto = self.esqder.y - self.esqiz.y
        return ancho == alto
    
p1 = pr(2, 1)
p2 =  pr(4, 2)
rec = rec(p1 , p2)

print("perimetro es", rec.calperimetro())
print("area es", rec.calarea())
if rec.escua():
    print("es")
else:
    print("no es")
    
    

        


