class Node:
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



class DoublyLk:
    def __init__(self):
        self.font = Node(None)
        self.back = Node(None)
        self.head = self.font
        self.tail = self.back
        self.font.next = self.back
        self.font.prev = None
        self.back.prev = self.font
        self.back.next = None
    def __str__(self):
        t = self.font
        strt = ""
        if t.next is None:
            return strt
        else:
            while t.next is not self.back:
                t = t.next
                strt += str(t.data) + " "
            return strt

    def reversedStr(self):
        t = self.back
        strt = ""
        if t.prev is self.font:
            return strt
        else:
            while t.prev != self.font:
                t = t.prev
                strt += str(t.data) + " "
            return strt

    def isEmpty(self):
        return self.font.next == None

    def size(self):
        t = self.font
        count = 0
        if self.isEmpty():
            return count
        else:
            while t.next is not self.back:
                t = t.next
                count += 1
            return count                    

    def append(self,data):
        t = self.font
        p = Node(data)
        if self.isEmpty():
            self.font.next = p
            p.prev = self.font
            self.back.prev = p
            p.next = self.back
        else:
            while t != self.back:
                t = t.next
            p.next = self.back
            p.prev = self.back.prev
            self.back.prev.next = p
            self.back.prev = p

    def addHead(self, data):
        t = self.font
        p = Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            p.next = self.font.next
            p.prev = self.font
            self.font.next.prev = p
            self.font.prev = None
            self.font.next = p

    def search(self, data):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return "Not Found"
        else:
            while t.next is not self.back:
                if t.data == data:
                    return count
                else:
                    t = t.next
                    count += 1
            if t.data == data:
                return count
            else:
                return "Not Found"

    def index(self, items):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return -1
        else:
            while t is not self.back:
                if t.data == items:
                    return count
                else:
                    t = t.next
                    count += 1
            return count 

    def pop(self, index):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return "Empty"
        else:
            while t is not self.back:
                if self.index(t.data) == index:
                    break
                else:
                    t = t.next
            if t is not self.back:
                t.prev.next = t.next
                t.next.prev = t.prev
                t.next = None
                t.prev = None
            else:
                return "Out of Range"

    def insert(self , index, data):
        t = self.font.next
        p = Node(data)
        if self.isEmpty():
            self.addHead(data)
        else:
            while t is not self.back:
                if self.index(t.data) == index:
                    break
                else:
                    t = t.next
            if t is not self.back:
                p.next = t
                p.prev = t.prev
                t.prev.next = p
                t.prev = p
            else:
                t = t.prev
                self.append(data)

    def moveleft(self):
        t = self.font.next
        p = Node("|")
        if self.size() == 1 or self.isEmpty():
            return
        elif self.index("|") == 0:
            return    
        else:
            while t.data != "|":
                t = t.next
            if t.data == '|':
                r = t.prev
                self.insert(self.index(t.prev.data), '|')
                t.next.prev = t.prev
                t.prev.next = t.next
                t.prev = None
                t.next = None

    def moveRight(self):
        t = self.font.next
        p = Node("|")
        if self.size() == 1 or self.isEmpty():
            return
        elif self.index("|") == self.size() - 1:
            return    
        else:
            while t.data != "|":
                t = t.next
            if t.data == '|':
                r = t.next
                self.insert(self.index(t.next.next.data), '|')
                t.next.prev = t.prev
                t.prev.next = t.next
                t.prev = None
                t.next = None 

    def removeLeft(self):
        t = self.font.next
        if self.size() == 1 or self.isEmpty():
            return
        elif self.index("|") == 0:
            return    
        else:
            while t.data != "|":
                t = t.next
            if t.data == '|':
                self.pop(self.index(t.prev.data))

    def removeRight(self):
        t = self.font.next
        if self.size() == 1 or self.isEmpty():
            return
        elif self.index("|") == self.size() - 1:
            return 
        else:
            while t.data != "|":
                t = t.next
            if t.data == '|':
                self.pop(self.index(t.next.data))            
                                  


lk = DoublyLk()
inp = input("Enter Input : ").split(',')
lk.append("|")
for i in inp:
    a = i.split()
    if a[0] == 'I':
        if lk.size() == 1:
            lk.addHead(a[1])
        else:
            j = lk.search("|")
            lk.insert(j,a[1])
    elif a[0] == 'L':
        lk.moveleft() 
    elif a[0] == 'R':
        lk.moveRight() 
    elif a[0] == 'B':
        lk.removeLeft()
    elif a[0] == 'D':
        lk.removeRight()                
print(lk)        