__author__ = 'cgiridhar'

from collections import deque

# Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”).
# Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1)
# performance in either direction.

#Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n)
# memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

deque = range(9)
deque.append("1")
print deque

deque.pop()
print deque