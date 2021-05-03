class Queue:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def enQueue(self, i):
        self.items.append(i)
    def enQueueinsert(self, index, i):
        self.items.insert(index,i)    
    def deQueue(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def peekFull(self):
        return self.items
    def indexNum(self, inp):
        return q.items.index(inp)
member, comb = input("Enter Input : ").split('/')
q = Queue()
isEn = False
mem = [mem.split() for mem in member.split(',')]
memdict = {}
for i in mem:
    m = {i[1]:i[0]}
    memdict.update(m)
for i in comb.split(','):
    temp = i.split()
    if q.isEmpty():
        if temp[0] == 'D':
            print("Empty")
        else:
            q.enQueue(temp[1])    
    else:
        if temp[0] == 'E':
            for j in reversed(q.items):
                if memdict[temp[1]] == memdict[j]:
                    q.enQueueinsert(q.indexNum(j) + 1, temp[1])
                    isEn = True
                else:
                    pass
            if isEn == False:    
                q.enQueue(temp[1])
            else:
                isEn = False    
        else:
            if q.isEmpty():
                print("Empty")
            else:
                print(q.deQueue())    

                                
    
