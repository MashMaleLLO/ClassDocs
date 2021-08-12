class Stack:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def peek2(self):
        return self.items[-2]
    def peekFull(self):
        return self.items

inp = [inp for inp in input("Enter Input : ").split()]
s = Stack()
count = 0
j = 0
combo = 0
strt = ''
for i in inp:
    if s.isEmpty():
            s.push(i)
    else:
        if s.size() > 1:
            if s.peek() == i and s.peek2() == i:
                s.pop()
                s.pop()
                combo += 1
            else:
                s.push(i)
        else:
            s.push(i)  

print(s.size())
if s.size() == 0:
    print("Empty")
else:
    for i in range(s.size()):
        strt += s.pop()
    print(strt)
if combo >= 2:
    print("Combo : {} ! ! !".format(combo))
else:
    pass            

"""
test case 

Enter Input : 1 2 2 3 4
5
43221

Enter Input : a b b c d d e d
8
deddcbba

Enter Input : a a a a b c e
4
ecba


Enter Input : b a a a b b c a a a c c
0
Empty
Combo : 4 ! ! !


"""