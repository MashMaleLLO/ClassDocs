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
    def peek(self):
        return self.items[0]
    def peekFull(self):
        return self.items

def enCoder(ls,cipher):
    j = 0
    count = 0
    while j < len(ls) - 1:
        for i in ls:
            i = ord(i)
            if count == len(cipher):
                count = 0
                if i + int(cipher[count]) > 90 and i + int(cipher[count]) < 97:
                    div = 90 - i
                    div = abs(div - int(cipher[count]))
                    i = 64 + div
                elif i + int(cipher[count]) > 122:
                    div = 122 - i
                    div = abs(div - int(cipher[count]))
                    i = 96 + div
                else:
                    i += int(cipher[count])
                count += 1    
            else:
                if i + int(cipher[count]) > 90 and i + int(cipher[count]) < 97:
                    div = 90 - i
                    div = abs(div - int(cipher[count]))
                    i = 64 + div
                elif i + int(cipher[count]) > 122:
                    div = 122 - i
                    div = abs(div - int(cipher[count]))
                    i = 96 + div
                else:
                    i += int(cipher[count])
                count += 1
            i = chr(i)
            q.enQueue(i)
            j += 1
            
              

def deCoder(ls,cipher):
    j = 0
    count = 0
    while j < len(ls) - 1:
        for i in ls:
            i = ord(i)
            if count == len(cipher):
                count = 0
                if i - int(cipher[count]) < 65:
                    div = i - 65
                    div = abs(div - int(cipher[count]))
                    i = 91 - div
                elif i -int(cipher[count]) < 97 and i >= 97:
                    div = i - 97
                    div = abs(div - int(cipher[count]))
                    i = 123 - div
                else:
                    i -= int(cipher[count])    
                count += 1             
            else:
                if i - int(cipher[count]) < 65:
                    div = i - 65
                    div = abs(div - int(cipher[count]))
                    i = 91 - div
                elif i -int(cipher[count]) < 97 and i >= 97:
                    div = i - 97
                    div = abs(div - int(cipher[count]))
                    i = 123 - div
                else:
                    i -= int(cipher[count])    
                count += 1        
            i = chr(i)
            q2.enQueue(i)
            j += 1


inp = [inp for inp in input("Enter String and Code : ").split(',')]
q = Queue()
q2 = Queue()
temp = list(inp[0])
cipher = list(inp[1])
for i in temp:
    if i == " ":
        temp.remove(i)
    else:
        pass   
enCoder(temp,cipher)
deCoder(q.items,cipher)
print("Encode message is :  {}".format(q.peekFull()))
print("Decode message is :  {}".format(q2.peekFull()))



