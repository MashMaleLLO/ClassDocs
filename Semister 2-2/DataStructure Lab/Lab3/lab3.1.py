class Stack:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def size(self):
        return len(self.items)             
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[-1]        
            


"""
test case

 *** Stack implement by Python list***
Enter data to stack : 1 2 3 4 5
5 Data in stack :  ['1', '2', '3', '4', '5']
0 Data in stack :  []


"""



print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:

    s.push(e)
print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()
print(s.size(),"Data in stack : ",s.items)