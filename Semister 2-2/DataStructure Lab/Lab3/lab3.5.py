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
        return self.items[-1] 

def lookingTree(stack):
    ns = stack.items.copy()
    ns = Stack(ns)
    highest = 0
    count = 0
    while not ns.isEmpty():
        if ns.peek() > highest:
            count += 1
            highest = ns.peek()
            ns.pop()
        else:
            ns.pop()
    return count

def seeingTree(inp):
    s = Stack()
    for i in inp:
        poi = Stack()
        highest = 0
        temp = i.split()
        if len(i) > 1:
            if len(i) > 3:
                o = ''
                for x in i[2::]:
                    o += x
                j = int(o)
                if j < 1:
                    pass
                else:
                    s.push(j)
            else:    
                j = int(i[2])
                s.push(j)
        elif i[0] == 'B':
            print(lookingTree(s))
        elif i[0] == 'S':
            if not s.isEmpty():
                for i in s.items:
                    if i%2 == 0 and i > 1:
                        i = i - 1
                        poi.push(i)
                    elif i == 1:
                        i = i + 2
                        poi.push(i)    
                    elif i%2 != 0 and i > 1:
                        i = i + 2
                        poi.push(i)
            else:
                pass            
            s = poi            

inp = [inp for inp in input("Enter Input : ").split(',')]
seeingTree(inp)

    
