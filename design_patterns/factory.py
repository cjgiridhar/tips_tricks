__author__ = 'cgiridhar'

from abc import ABCMeta, abstractmethod

class Abstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_say(self):
        pass

class Duck(Abstract):
    def do_say(self):
        print("Its Quacking")

class Horse(Abstract):
    def do_say(self):
        print("Its Naying")


class ForestFactory(object):
    def do_something(self, object_type):
        return eval(object_type)().do_say()

ff = ForestFactory()
ff.do_something('Duck')