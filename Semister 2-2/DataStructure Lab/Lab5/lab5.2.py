class node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
        if prev is None:
            self.prev = None
        else:
            self.prev = prev        

    def __str__(self):
        return str(self.data)

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        strt = "Linked List : "
        t = self.head
        if self.head == None:
            return "Linked List : Empty"
        else:
            while t.next is not None:
                if t == self.head:
                    strt += str(t.data) + ' '
                else:    
                    strt += str(t.data) + ' '
                t = t.next
            strt += str(t.data)
            return str(strt)
    
    def dataInLink(self):
        strt = ""
        t = self.head
        if self.head == None:
            return "list is empty"
        else:
            while t.next is not None:
                if t == self.head:
                    strt += str(t.data) + ' '
                else:    
                    strt += str(t.data) + ' '
                t = t.next
            strt += str(t.data)
            return str(strt)

    def reversedStr(self):
        strt = "Linked List Reverse : "
        t = self.tail
        if self.head == None:
            return "Linked List Reverse : Empty"
        else:
            while t.prev is not None:
                if t == self.tail:
                    strt += str(t.data) + ' '
                else:
                    strt += str(t.data) + ' '
                t = t.prev
            strt += str(t.data)
            return str(strt)                       

    def isEmpty(self):
        return self.head == None

    def size(self):
        t = self.head
        count = 0
        strt = "Linked List size = "
        if self.head == None:
            return str(strt + "{} : Empty".format(count))
        else:
            while t is not None:
                t = t.next
                count += 1
            return str(strt + "{} : {}".format(count,self.dataInLink()))

    def sizeNum(self):
        t = self.head
        count = 0
        if self.head == None:
            return count
        else:
            while t is not None:
                t = t.next
                count += 1
            return count

    def append(self, data):
        t = self.head
        p = node(data)
        if self.head == None:
            self.head = p
            self.tail = self.head
        else:
            while t.next is not None:
                t = t.next
            t.next = p
            p.prev = t
            self.tail = p

    def addHead(self, data):
        t = self.head
        p = node(data)
        if self.head == None:
            self.head = p
            p.next = None
            p.prev = None
            self.tail = self.head
        else:
            p.next = self.head
            p.prev = None
            self.head.prev = p
            self.head = p

    def search(self, items):
        t = self.head
        if self.head == None:
            return "Not Found"
        else:
            while t is not None:
                if t.data == items:
                    return "Found"
                else:
                    t = t.next
            return "Not Found" 

    def index(self, items):
        t = self.head
        count = 0
        if self.head == None:
            return -1
        else:
            while t is not None:
                if t.data == items:
                    return count
                else:
                    t = t.next
                    count += 1
            return -1

    def pop(self, index):
        t = self.head
        count = 0
        if self.head is None:
            return "Out of Range | Empty"
        else:
            if int(index) > int(self.sizeNum()) or int(index) < 0:
                return "Out of Range | {}".format(self.dataInLink())
            elif index == 0:
                if t.next is None:
                    i = self.head.data
                    self.head = None
                    self.tail = None
                    return "Success | {} -> Empty".format(i)
                else:
                    j = self.head.data
                    self.head.next.prev = None
                    self.head = self.head.next
                    return "Success | {} -> {}".format(j,self.dataInLink())
            else:
                while t.next is not None:
                    if count == index:
                        break
                    else:
                        t = t.next
                        count += 1
                if t.next is None:
                    if count == index:
                        r = t.data
                        self.tail = t.prev
                        t.prev.next = t.next
                        t.prev = None
                        return "Success | {} -> {}".format(r,self.dataInLink())
                    else:
                        return "Out of Range | {}".format(self.dataInLink())
                else:
                    k = t.data
                    t.prev.next = t.next
                    t.next.prev = t.prev
                    return "Success | {} -> {}".format(k,self.dataInLink())


    def insert(self, index, data):
        t = self.head
        p = node(data)
        index = int(index)
        count = 0
        negCount = -1
        negIndex = (1 * self.sizeNum())
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            if index >= 0:
                if index == 0:
                    p.next = self.head
                    self.head.prev = p
                    self.head = p
                else:
                    while t.next is not None:
                        if count + 1 == index:
                            break
                        else:
                            t = t.next
                            count += 1
                    if t.next is None:
                        t.next = p
                        p.prev = t
                        self.tail = p
                    else:
                        p.next = t.next
                        t.next.prev = p
                        t.next = p
                        p.prev = t
            else:
                if index == -1:
                    p.next = self.tail
                    p.prev = self.tail.prev
                    self.tail.prev.next = p
                    self.tail.prev = p
                else:
                    e = self.tail
                    while e.prev is not None:
                        if negCount == index:
                            break
                        else:
                            e = e.prev
                            negCount -= 1
                    if e.prev is None:
                        e.prev = p
                        p.next = e
                        p.prev = None
                        self.head = p
                    else:
                        p.next = e
                        p.prev = e.prev
                        e.prev.next = p
                        e.prev = p             




inp = input("Enter Input : ").split(',')
lk = linkedlist()
for i in inp:
    a = i.split()
    if a[0] == 'AP':
        lk.append(a[1])
    elif a[0] == 'PO':
        print(lk.pop(int(a[1])))
    elif a[0] == 'SI':
        print(lk.size())
    elif a[0] == 'AH':
        lk.addHead(a[1])
    elif a[0] == 'IS':
        lk.insert(a[1],a[2])
    elif a[0] == 'SE':
        print("{} {} in {}".format(lk.search(a[1]), a[1], lk.dataInLink()))
    elif a[0] == 'ID':
        print("Index ({}) = {} : {}".format(a[1], lk.index(a[1]), lk.dataInLink()))           
print(lk)
print(lk.reversedStr())  


    
    
