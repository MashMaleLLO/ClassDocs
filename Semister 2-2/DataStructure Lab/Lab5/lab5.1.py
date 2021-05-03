class node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)

class linkedlist:
    def __init__(self):
        self.head = None
    def __str__(self):
        strt = "link list : "
        t = self.head
        if self.head == None:
            return "List is empty"
        else:    
            while t.next != None:
                strt += str(t.data) + '->'
                t = t.next
            strt += str(t.data)
            return str(strt) 

    def isEmpty(self):
        return self.head == None

    def size(self):
        t = self.head
        count = 0
        while t is not None:
            count += 1
            t = t.next
        return count

    def append(self, data):
        p = node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p


    def insert(self, indexnum, data):
        t = self.head
        p = node(data)
        count = 0
        if self.head == None and indexnum <= self.size():
            print("index = {} and data = {}".format(indexnum, data))
            self.head = p
        else:
            t = self.head
            if indexnum < 0 or indexnum > self.size():
                print("Data cannot be added")
            else:    
                while t.next != None or self.size() < 2:
                    if count + 1 == indexnum:
                        print("index = {} and data = {}".format(indexnum, data))
                        p.next = t.next
                        t.next = p
                        break
                    elif indexnum == 0:
                        print("index = {} and data = {}".format(indexnum, data))
                        p.next = self.head
                        self.head = p
                        break
                    else:
                        t = t.next
                        count += 1
                else:
                    print("index = {} and data = {}".format(indexnum, data))
                    t.next = p               

inp = input("Enter Input : ").split(',')
lk = linkedlist()
index = []
for a in inp[0].split():
    lk.append(a)
print(lk)
if len(inp[0]) == 0:
    for a in inp[1:]:
        st = ''
        for i in a:
            st += i
        num = ''
        for s in st:
            if s != ':':
                num += s
            else:
                index.append(int(num))
                num = ''
        index.append(num)
        lk.insert(index[0],index[1])
        print(lk)
        index = []   
else:
    for a in inp[1:]:
        st = ''
        for i in a[1:]:
            st += i
        num = ''
        for s in st:
            if s != ':':
                num += s
            else:
                index.append(int(num))
                num = ''
        index.append(num)
        lk.insert(index[0],index[1])
        print(lk)
        index = []   

