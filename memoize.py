__author__ = 'cgiridhar'

from datetime import datetime

def memoize(fn):
    memo = {}
    def helper(arg):
        if arg not in memo.keys():
            memo[arg] = fn(arg)
        return memo[arg]
    return helper

@memoize
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+ fib(n-2)

print fib(6)




#====================================

def memo(f, arg):
    mem = {}
    if arg not in mem.keys():
        mem[arg] = f(arg)
    return mem[arg]


@memo
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print fact(5)