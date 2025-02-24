import matplotlib.pyplot as plt

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
 
    def __str__(self):
        return f"({self.x},{self.y})"

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    

class Linea:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self):
        return f"Linea de {self.p1} a {self.p2}"
    
    def dibujaLinea(self):
        x = [self.p1.getX(), self.p2.getX()]
        y = [self.p1.getY(), self.p2.getY()]
        plt.plot(x,y, marker='o', linestyle='-')
        plt.show()
        
       

class Circulo:
    def __init__(self,c,r):
        self.centro = c
        self.radio = r

    def __str__(self):
       return f"Circulo con centro {self.centro} y radio {self.radio}"

    def dibujaCirculo(self):
        c = (self.centro.getX(), self.centro.getY())
        r = self.radio
        
        fig, ax = plt.subplots()
        
        circulo = plt.Circle(c, r, color='b', fill=False)
        
        ax.add_patch(circulo)
        ax.set_xlim(c[0] - r - 1, c[0] + r + 1)
        ax.set_ylim(c[1] - r - 1, c[1] + r + 1)
        ax.set_aspect('equal')
        plt.show()

       


p1 = Punto(1,2)
p2 = Punto(5,4)
linea = Linea(p1, p2)

print(linea)
linea.dibujaLinea()

p = Punto(5,5)
circulo = Circulo(p, 3)
print(circulo)
circulo.dibujaCirculo() 

print(circulo)
print(circulo.dibujaCirculo())

