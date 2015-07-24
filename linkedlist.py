__author__ = 'cgiridhar'
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = Node(None, None)

    def insert(self, data):
        if self.first == None:
            self.first = Node(data, self.last)
        else:
            temp = self.first
            while temp.next != self.last:
                temp = temp.next
            temp.next = Node(data, self.last)

        return self.first

    def show(self):
        temp = self.first
        while temp != self.last:
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.insert(5)
ll.insert(15)
ll.show()