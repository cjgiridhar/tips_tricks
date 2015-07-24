__author__ = 'cgiridhar'

class A:
    __slots__ = ["var"]
    __b = 10
    var = 11
    value = 12

    def __setB(self,b):
        self.__b = b

    def a(self):
        pass

a = A()
## print a.__b not accessible
a.a()
## a.__setB(11)
print a.value


class Point(object):
    __slots__=["x", "y"]

p = Point()
p.x = 10
p.y = 20   # this are OK
p.z = 30   # this causes AttributeError: 'Point' object has no attribute 'z'