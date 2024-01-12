class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        sarea = self.base * self.altura
        print(sarea)

    def perimetro(self):
        sperimetro = (self.base + self.altura) * 2
        print(sperimetro)