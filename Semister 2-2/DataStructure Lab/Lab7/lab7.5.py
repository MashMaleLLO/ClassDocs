class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def __str__(self):
        strt = ''
        if self.items == []:
            return "Empty"
        else:
            for i in self.items:
                strt += str(i) + " "
            return strt
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]

class Queue:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def __str__(self):
        strt = ''
        if self.items == []:
            return "Empty"
        else:
            for i in self.items:
                strt += str(i) + " "
            return strt
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enQueue(self, data):
        self.items.append(data)
    def deQueue(self):
        return self.items.pop(0)
    def head(self):
        return self.items[0]

class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if curr.data > data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root
    def print_tree(self, node, level = 0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print("     " * level,node)
            self.print_tree(node.left, level + 1)

    

pre = "Prefix : "
post = " "
ino = "Infix : "
    
def preorder(node):
    global pre
    if node is not None:
        pre += str(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(curr):
    global post
    if curr is not None:
        postorder(curr.left)
        postorder(curr.right)
        post += str(curr.data) 

def inorder(curr):
    global ino
    if curr is not None:
        if curr.left is not None or curr.right is not None:  # not leaf
            ino += "("
        inorder(curr.left)
        ino += str(curr.data)
        inorder(curr.right)
        if curr.left is not None or curr.right is not None:  # not leaf
            ino += ")"


b = BST()
oparand = Stack()
inp = input("Enter Postfix : ")
for i in inp:
    if i in "+-*/^":
        a = Node(i)
        a.right = oparand.pop()
        a.left = oparand.pop()
        oparand.push(a)
    else:
        a = Node(i)
        oparand.push(a)
b.root = oparand.pop()
print("Tree :",end='\n')
b.print_tree(b.root)
print("--------------------------------------------------")
inorder(b.root)
preorder(b.root)
print(ino)
print(pre)


