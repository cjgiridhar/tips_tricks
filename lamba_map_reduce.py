__author__ = 'cgiridhar'
g = lambda x : x*2
print g(4)

a = map(g, range(9))
print a

aa = reduce(lambda x,y: x+y, range(0,9))
print aa

aaa = filter(lambda x:x%3==0, range(9))
print aaa

