class Carta:
    PINTA_CORAZONES = "Corazones"
    PINTA_DIAMANTES = "Diamantes"
    PINTA_TRÉBOLES = "Tréboles"
    PINTA_PICAS = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor  
        self.pinta = pinta   

carta1 = Carta("as", Carta.PINTA_CORAZONES)
carta2 = Carta("rey", Carta.PINTA_PICAS)

print("Carta 1", carta1.valor, "de", carta1.pinta)
print("Carta 2", carta2.valor, "de", carta2.pinta)
 #porfe, esta la hice mayormente con ia, no la entendi muy bien
