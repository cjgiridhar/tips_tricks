__author__ = 'cgiridhar'
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarTree:

    def __init__(self):
        self.root = None
        self.N = 0

    def insert(self, data):
        def insertIntoBST(node, data):
            if node is None:
                return Node(data)
            if data <= node.data:
                node.left = insertIntoBST(node.left, data)
            else:
                node.right = insertIntoBST(node.right, data)
            return node
        self.root = insertIntoBST(self.root, data)

    def inorder(self):
        def inorderPrint(node):
            if node is None:
                return
            inorderPrint(node.left)
            print(str(node.data) + " ",
            inorderPrint(node.right))
        inorderPrint(self.root)


def main():
    bt = BinarTree()
    values = [8, 5, 13, 2, 7, 10, 15]
    for v in values:
        bt.insert(v)
    bt.inorder()

if __name__ == '__main__':
    main()