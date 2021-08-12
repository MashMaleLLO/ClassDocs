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
    def peekFull(self):
        return self.items

def highLander(i,j):
    dic = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':0} 
    if dic[i] < dic[j]:
        return True
    elif dic[i] == dic[j]:
        return False    
    else:
        return False      

def infixTopostfix(exp):
    s = Stack()
    ope = ['+','-','*','/','^','(',')']
    post = ''
    for i in exp:
        if i in ope:
            if s.isEmpty():
                s.push(i)
            else:
                if i == '(':
                    s.push(i)
                elif i in '+-*/^':
                    while s.size() != 0 and highLander(s.peek(), i) is False:
                        if s.peek() == '(':
                            s.pop()
                        else:    
                            post += s.pop()
                    s.push(i)
                else:
                    while s.size() != 0 and s.peek() != '(':
                        post += s.pop()
                    if s.isEmpty():
                        pass
                    else:
                        s.pop()    
        else:
            post += i                    
            
    while not s.isEmpty():
        post += s.pop()
    else:
        pass                
    return post                   





print(" ***Infix to Postfix***")
inp = [inp for inp in input("Enter Infix expression : ")]
print("PostFix :")
print(infixTopostfix(inp))

"""

test case

***Infix to Postfix***
Enter Infix expression : a+b*c
PostFix :
abc*+

***Infix to Postfix***
Enter Infix expression : ((a/b)*c)^d
PostFix :
ab/c*d^




"""

