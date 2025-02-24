import math

class punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return (self.x , self.y)

    def coord_polares(self):
        radio = math.sqrt(self.x * self.x + self.y * self.y)
        angulo = math.sqrt(self.y/self.y)
        angulo = math.degrees(angulo)
        return radio, angulo

    def __str__(self):
        return "({:.2f},{:.3f})" .format(self.x, self.y)

p = punto(5,7)
print(p)
x,y = p.coord_cartesianas()
print(x,y)
r,a = p.coord_polares()
print(r,a)