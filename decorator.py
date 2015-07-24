__author__ = 'cgiridhar'
from datetime import datetime

def time(fn):
    def wrap(arg):
        startTime = datetime.now()
        fn(arg)
        endTime = datetime.now()
        print(endTime - startTime)
    return wrap

@time
def fact(n):
    if n == 0 or n == 1:
        return 1
    f = 1
    for i in range(1,n):
        f *= i
    return f

#fact(100)


##########################################
class Decorator(object):
    def __init__(self,f):
        self.f = f

    def __call__(self, args):
        startTime = datetime.now()
        print self.f(args)
        endTime = datetime.now()
        print "Time taken", endTime - startTime


@Decorator
def isPrime(n):
    if n==2:
        return 1
    if n<0 or n%2==0:
        return -1
    for i in range(2,n):
        if n % i == 0:
            return -1
    return 1

isPrime(5)


#=========================================


class ClassMemo:
    """This is a decorator"""
    def __init__(self,fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo.keys():
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]


def fnMemo(fn, arg):
    memo = {}
    if arg not in memo.keys():
        memo[arg] = fn(arg)
        return memo[arg]


def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


startTime = datetime.now()
print fib(150)
print fnMemo(fib,150)
endTime = datetime.now()
print "Time taken", endTime - startTime
