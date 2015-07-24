__author__ = 'cgiridhar'

from abc import abstractmethod, ABCMeta

class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def help(self):
        pass


class rm(Command):
    def execute(self):
        print("Executing... rm command")

    def help(self):
        print("Executing... rm help")

class mv(Command):
    def execute(self):
        print("Executing... mv command")

    def help(self):
        print("Executing... mv help")



class Client(object):
    def execute(self, obj):
        eval(obj)().execute()


cl = Client()
cl.execute("rm")