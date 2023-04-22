class point:
   
    def __init_(self, x, y):
        self.x = x
        self.y = y
   
       
class circle(point):
    def __init_(self, x, y, raio):
        super().__init__(x, y)
        self.raio = raio
       
    def calcule_area(self):
        area = 3.14 * (self.raio) ** 2
        return area
       
    def calcule_perimeter(self):
        perimeter = 2 * 3.14 * self.raio
        return perimeter
        
    def show(self):
        print("Coordenadas do Circulo:")
        print("Centro: ({}, {})".format(self.x, self.y))
        print("Raio: {}".format(self.radius))
        
class triangle(point):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.points = [point(x1, y1), point(x2, y2), point(x3, y3)]
        
    def calcule_area(self):
        a = self.side(self.points[0], self.points[1])
        b = self.side(self.points[1], self.points[2])
        c = self.side(self.points[2], self.points[0])
        z = (a + b + c) / 2 
        area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
        return area
        
    def calcule_perimeter(self):
        a = self.side(self.points[0], self.points[1])
        b = self.side(self.points[1], self.points[2])
        c = self.side(self.points[2], self.points[0])
        z = (a + b + c)
        perimetro = a + b + c
        return perimeter
        
    def side(self, p1, p2):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
        
    def show(self):
        print("Coordenadas do triangulo:")
        print("Ponto 1: ({}, {})".format(self.point1.x, self.point1.y))
        print("Ponto 2: ({}, {})".format(self.point2.x, self.point2.y))
        print("Ponto 3: ({}, {})".format(self.point3.x, self.point3.y))
        
class retangle(point):
    def __init__(self, x1, y1, x2, y2):
        self.point1 = [point(x1, y1)]
        self.point2 = [point(x2, y2)]
        
    def calcule_area(self):
        base = abs(self.point1.x - self.point2.x)
        altura = abs(self.point1.y - self.point2.y)
        area = base * altura
        return area
        
    def calcule_perimeter(self):
        bese = abs(self.point1.x - self.point2.x)
        altura = abs (self.point1.y - self.point2.y)
        perimetro = 2 * (base * altura)
        return perimeter
        
    def show(self):
        print("Coordenadas do retângulo:")
        print("Ponto 1: ({}, {})".format(self.p1.x, self.p1.y))
        print("Ponto 2: ({}, {})".format(self.p2.x, self.p2.y))
