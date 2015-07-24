__author__ = 'cgiridhar'
def myrange(n):
    i = 0
    while(i<n):
        yield i
        i+1

print myrange(9)
y = myrange(8)
print y.next()

def fib():
    a,b = 0, 1
    while True:
        yield a
        a,b = b,a+b

x = fib()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()

# https://wiki.python.org/moin/Generators -- Generator vs list (xrange vs range)
#Note that both lines are identical in form, but the one using range is much more expensive.

#When we use range we build a 1,000,000 element list in memory and then find its sum. This is a waste, considering that we use these 1,000,000 elements just to compute the sum.
#This waste becomes more pronounced as the number of elements (our n) becomes larger, the size of our elements become larger, or both.
#On the other hand, when we use xrange, we do not incur the cost of building a 1,000,000 element list in memory. The generator created by xrange will generate each number, which sum will consume to accumulate the sum.
#In the case of the "range" function, using it as an iterable is the dominant use-case, and this is reflected in Python 3.x, which makes the range built-in return a generator instead of a list.
#Note: a generator will provide performance benefits only if we do not intend to use that set of generated values more than once.