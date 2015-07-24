__author__ = 'cgiridhar'
from abc import ABCMeta, abstractmethod

class Abstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_something(self):
        pass

class MyKls(Abstract):
    pass
    # def do_something(self):
    #     pass

#abs = Abstract()
mykls = MyKls()
mykls.do_something()