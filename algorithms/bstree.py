__author__ = 'cgiridhar'

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BSTree:

    def __init__(self):
        pass

    def insert(self, root, data):
        if root is None:
            root = Node(data)
            return True

        if data < root.data:
            if root.left is None:
                root.left = Node(data)
                return True
            else:
                self.insert(root.left, data)

        if data > root.data:
            if root.right is None:
                root.right = Node(data)
                return True
            else:
                self.insert(root.right, data)

    def preorder(self, root):
        if root is None:
            return "No Elements!"
        else:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return "No Elements!"
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)


    def search(self, root, item):
        if root.data == item:
            print(root.data)
        if item < root.data:
            self.search(root.left, item)
        if item > root.data:
            self.search(root.right, item)


#######################
bst = BSTree()
root = Node(10)

#######################
bst.insert(root, 5)
bst.insert(root, 3)
bst.insert(root, 7)
bst.insert(root, 11)

#######################
bst.preorder(root)
print("----------")
bst.inorder(root)

#######################
#bst.search( bst.my_root(), 3)