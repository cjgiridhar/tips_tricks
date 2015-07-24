__author__ = 'cgiridhar'
#http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example
class MyType(type):
    def __new__(meta, name, bases, dict):
        print("Creating Object")
        print("Meta is:" , meta)
        print("Name is:", name)
        return super(MyType, meta).__new__(meta, name, bases, dict)

    def __init__(cls, name, bases, dict):
        print("Initializing Object")
        print("Name is:", name)
        super(MyType, cls).__init__(name, bases, dict)

class MyMetaClass(object):
    __metaclass__ = MyType
    foo = "bar"

mc = MyMetaClass()
print(mc)

foo = type('Foo', (object,), {})
print(type(foo))


def set_x(self, value):
    self.x = value

SubClass = type('SubClass', (object,), {'set_x': set_x})
obj = SubClass()
obj.set_x(42)
print(obj.x)  #




class MetaSingleton(type):
    instance = None
    def __call__(cls, name, bases, dict):
        if cls.instance is None:
            cls.instance+=1
            return super(MetaSingleton, cls).__call__(name, bases, dict)


class Foo(object):
     __metaclass__ = MetaSingleton

a = Foo()
b = Foo()
#a()
print(a, b)
assert a is not b



test = type('Test', (object,), dict(a=10))
print(test().a)