__author__ = 'cgiridhar'

from abc import abstractmethod, ABCMeta

class Line(object):
    def draw(self,x,y):
        print("Line is between points", x, "and", y)

class Rectangle(object):
    def draw(self, x,y):
        print("Rectangular coordinates", x, "and", y)


class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass

class LineShape(Shape):
    def draw(self,x,y):
        self.adaptee = Line()
        self.adaptee.draw(x,y)

class RectangleShape(Shape):
    def draw(self,x,y):
        self.adaptee = Rectangle()
        self.adaptee.draw(x,y)


class Client():
    def draw(self,x,y):
        objects = [LineShape(), RectangleShape()]
        for obj in objects:
            obj.draw(x,y)

cl = Client()
cl.draw(3,5)