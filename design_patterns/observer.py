__author__ = 'cgiridhar'

from abc import abstractmethod, ABCMeta

class Publisher(object):

    __subscribers = []
    def register(self, obj):
        print("Object registered:", obj)
        self.__subscribers.append(obj)

    def unregister(self, obj):
        print("Object unregistered:", obj)
        self.__subscribers.remove(obj)

    def notifyAll(self):
        for sub in self.__subscribers:
            sub.update()

    def notify(self, sub):
        sub.update()

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass

class Observer1(Observer):
    def update(self):
        print("Observer1 is getting notified")

class Observer2(Observer):
    def update(self):
        print("Observer2 is getting notified")

pub = Publisher()
for obj in [Observer1(), Observer2()]:
    pub.register(obj)

pub.notifyAll()
