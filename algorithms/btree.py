__author__ = 'cgiridhar'

class Node():
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

class BTree():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        if self.root:
            if self.root.left is None:
                self.root.left = Node(data)
                return True
            else:
                self.insert(self.root.left, data)

            if self.root.right is None:
                self.root.right = Node(data)
                return True
            else:
                self.insert(self.root.right, data)

    def inorder(self, root):
        self.root = root
        if self.root is None:
            return "No Elements"
        else:
            self.inorder(self.root.left)
            print(self.root.data)
            self.inorder(self.root.right)


bt = BTree()
bt.insert(9)
bt.insert(3)
bt.insert(11)