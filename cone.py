# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from math import pi, sqrt

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    # Initialize the Circle object with a given radius
    def __init__(self, radius, **kwargs):
        self.radius = radius
        super().__init__(**kwargs)

    # Calculate and return the area of the circle using the formula: π * r^2
    def area(self):
        return pi * self.radius**2

    # Calculate and return the perimeter of the circle using the formula: 2π * r
    def perimeter(self):
        return 2 * pi * self.radius

    def __repr__(self):
        return f'Circle({self.radius})'

    def __str__(self):
        r0 = self.radius
        r1, r2 = self.area(), self.perimeter()
        return "Circle({0},{1} u^2,{2} u)".format(r0,r1,r2)

class Triangle(Shape):
    """
    Clase de los triángulo para la formación de los mismos,
    de ser posible, y la obtención de su área y perímetro.
    """
    # decides whether a triad of numbers forms a triangle or not
    def _es_triangulo(self, a, b, c):
        lst = [a,b,c]
        lst.sort()
        longer = lst.pop()
        return sum(lst) > longer

    # Calculates the semi-perimeter of a triangle
    def _semiperimeter(self):
        return (self.side1 + self.side2 + self.side3) / 2

    # Initialize the Triangle object with three side lengths if possible
    def __init__(self, side1, side2, side3, **kwargs):
        if self._es_triangulo(side1,side2,side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            self.side1, self.side2, self.side3 = 0, 0, 0
        super().__init__(**kwargs)

    # Calculate and return the area of the triangle using the formula: 0.5 * base * height
    def area(self):
        sp1, sp2, sp3 = self.side1, self.side2, self.side3
        sp = self._semiperimeter()
        return sqrt(sp*(sp-sp1)*(sp-sp2)*(sp-sp3))

    # Calculate and return the perimeter of the triangle by adding the lengths of its three sides
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __repr__(self):
        return f'Triangle({self.side1},{self.side2},{self.side3})'

    def __str__(self):
        s0,s1,s2 = self.side1, self.side2, self.side3
        s3, s4 = self.area(), self.perimeter()
        return "T({0},{1},{2},{3} u^2,{4} u)".format(s0,s1,s2,s3,s4)

class Cone(Triangle, Circle):
    """
    Clase Cone para definir y utilizar ramas de cono truncadas
    por un plano horizontal.
    """

    def _pitagoras(self,side1,side2):
        return sqrt(side1**2+side2**2)

    def __init__(self, radius, height, **kwargs):
         generatrix = self._pitagoras(radius,height)
         super().__init__(side1=radius, side2=height, side3=generatrix, radius=radius, **kwargs)

    def lateral_area(self):
        return pi * self.radius * self.side3

    def total_area(self):
        return self.lateral_area() + Circle.area(self)

    def volume (self):
        return Circle.area(self) * self.side2 / 3

    def __repr__(self):
        return f'Cone({self.radius},{self.side2})'

    def __str__(self):
           return Circle.__str__(self) + ", " + Triangle.__str__(self)


if __name__ == '__main__':
    c = Cone(3, 5)
    print(f'{c.volume()=}, {c.radius=}')
