class Queue:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enQueue(self, i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)

inp = [inp for inp in input("Enter Input : ").split(',')]
q = Queue()
strt = ''
for i in inp:
    if len(i) > 1:
        o = ''
        for j in i[2::]:
            o += j
        o = int(o)
        q.enQueue(o)
        print(q.size())
    else:
        if q.isEmpty():
            print("-1")
        else:
            print("{} 0".format(q.deQueue()))

if q.isEmpty():
    print("Empty")
else:               
    for i in q.items:
        strt += str(i) + " "
    print(strt)    


