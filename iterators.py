__author__ = 'cgiridhar'

class myrange(object):
    """ this is an interator"""
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        """The __iter__() method is called whenever someone calls iter(fib).
        (As youll see in a minute, a for loop will call this automatically, but you can also call it yourself manually.)
        After performing beginning-of-iteration initialization (in this case, resetting self.a and self.b, our two counters),
        the __iter__() method can return any object that implements a __next__() method.
        In this case (and in most cases), __iter__() simply returns self, since this class implements its own __next__() method."""
        return self

    def __next__(self):
        cur, self.i = self.i, self.i+1
        if cur < self.n:
            return cur
        else:
            raise StopIteration


#The for loop calls Fib(1000) as shown. This returns an instance of the Fib class. Call this fib_inst."""
#Secretly and quite cleverly, the for loop calls iter(fib_inst), which returns an iterator object. Call this fib_iter. In this case fib_iter == fib_inst, because the __iter__() method returns self but the for loop doesnt know (or care) about that."""
#To loop through the iterator, the for loop calls next(fib_iter), which calls the __next__() method on the fib_iter object, which does the next-Fibonacci-number calculations and returns a value. The for loop takes this value and assigns it to n, then executes the body of the for loop for that value of n."""
#How does the for loop know when to stop? Im glad you asked! When next(fib_iter) raises a StopIteration exception, the for loop will swallow the exception and gracefully exit. (Any other exception will pass through and be raised as usual.) And where have you seen a StopIteration exception? In the __next__() method, of course"""

print myrange(9)
m = myrange(8)
for my in myrange(10):
    print(my, ' ')