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
    def enQueueInsert(self, index, i):
        self.items.insert(index, i)    
    def deQueue(self):
        return self.items.pop(0)
    def seeing(self):
        return self.items[0]
    def seeFull(self):
        return self.items

inp = [inp for inp in input("Enter Input : ").split(',')]
q = Queue()
strt = ""
lis = []
isES = False
k = 0
for i in inp:
    if len(i) > 1:
        o = ''
        for j in i[3::]:
            o += j
        o = int(o)    
        if i[0:2] == "ES":
            if isES == False:
                isES = True
                q.enQueueInsert(0, o)
                k += 1
            else:
                q.enQueueInsert(k, o)
                k += 1    
        elif i[0:2] == "EN":
            q.enQueue(o)
    else:
        if q.isEmpty():
            lis.append("Empty")
        else:
            lis.append(q.seeing())
            q.deQueue()
            k = 0  
for i in lis:
    print(i,end='\n')



