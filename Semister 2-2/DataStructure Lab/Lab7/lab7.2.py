class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        p = Node(data)
        if self.root is None:
            self.root = p
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = p
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = p
                        break
                    curr = curr.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def findMin(self):
        if self.root is None:
            return -1
        else:
            curr = self.root
            while curr.left is not None:
                curr = curr.left
            return curr.data

    def findMax(self):
        if self.root is None:
            return -1
        else:
            curr = self.root
            while curr.right is not None:
                curr = curr.right
            return curr.data

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min : {}".format(T.findMin()))
print("Max : {}".format(T.findMax()))
