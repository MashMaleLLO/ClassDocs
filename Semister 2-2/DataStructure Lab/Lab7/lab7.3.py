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
    

lst = []


def inorderUntil(node, n):
    global lst
    if node != None:
        inorderUntil(node.left, n)
        if node.data > n:
            return
        inorderUntil(node.right, n)
        if node.data <= n:
            lst.append(str(node.data))
        return
            


T = BST()
inp = input("Enter Input : ").split('/')
k = int(inp[1])
for i in inp[0].split():
    root = T.insert(int(i))
T.printTree(root)
inorderUntil(root,k)
print("--------------------------------------------------")
print(len(lst))

