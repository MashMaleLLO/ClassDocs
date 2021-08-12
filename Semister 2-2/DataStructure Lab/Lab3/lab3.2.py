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
    def see(self):
        return self.items

def isMatch(i,j):
    opeP = "([{"
    closeP = ")]}"
    if i in opeP and j in opeP:
        return False
    elif i in closeP and j in closeP:
        return False    
    else:
        if i == '(' and j == ')':
            return True
        elif i == '[' and j == ']':
            return True
        elif i == '{' and j == '}':
            return True
        else:
            return False            



inp = [inp for inp in input("Enter expresion : ")]
s = Stack()
opeP = "([{"
closeP = ")]}"
match = False
strt = ''
lenSt = s.size()
end = False
for i in inp:
    strt += i

for i in inp:
    if i in opeP:
        s.push(i)
    elif i in closeP:
        if s.isEmpty():
            strt = ''
            for j in inp:
                strt += j
            print("{} close paren excess".format(strt))
            match = False
            end = True
            break  
        else:
            if isMatch(s.pop(), i) is True:
                match = True
            elif isMatch(s.pop(), i) is False:
                match = False
                break
            else:
                match = False
                break 
    else:
        pass          

strt2 = ''
for i in s.items:
    if s.isEmpty():
        strt2 += None
    else:
        strt2 += i


if not s.isEmpty():
    if end == False:
        print("{} open paren excess   {} : {}".format(strt, s.size(),strt2))
    else:
        pass    
else:
    if match is True:
        print("{} MATCH".format(strt))
    else:
        if end == False:
            print("{} Unmatch open-close".format(strt)) 
        else:
            pass       

"""

test case

Enter expresion : {(())}
{(())} MATCH

Enter expresion : {[()
{[() open paren excess   2 : {[

Enter expresion : {{()}}}
{{()}}} close paren excess

Enter expresion : {{{()}}
{{{()}} open paren excess   1 : {

"""
                                  

        