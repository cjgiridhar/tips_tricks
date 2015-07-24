__author__ = 'cgiridhar'

## Pipes provide duplex communication

from multiprocessing import Pipe, Process

def f(conn):
    conn.send(["hi"])
    conn.close()

parent,child = Pipe()
p = Process(target=f, args=(child,))
p.start()
print parent.recv()
p.join()


#####################################

from multiprocessing import Queue
import random

q = Queue()
def insert(q):
    for i in range(10):
        q.put(random.random())
    q.put('DONE')

def read(q):
    while True:
        print q.get()
        if(q.get == 'DONE'):
            break

# p1 = Process(target=insert, args=(q,))
# p1.start()
p2 = Process(target=read, args=(q,))
p2.daemon = True
p2.start()
insert(q)
p2.join()