__author__ = 'cgiridhar'
class Singleton(object):
    attr = 0

    def __new__(cls, *args, **kwargs):
        if Singleton.attr:
            raise Exception
        Singleton.attr = 1
        return super(Singleton,cls).__new__(cls, *args, **kwargs)

s = Singleton()
print(s)
#s1 = Singleton()

####################

class LogHandler:
    classAttr = None

    def __new__(cls, *args, **kwargs):
        if LogHandler.classAttr:
            raise Exception
        LogHandler.classAttr = 1
        return super(LogHandler, cls).__new__(cls, *args, **kwargs)

log = LogHandler()