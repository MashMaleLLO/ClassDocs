def deCoder(inp):
    i = 0
    while i <= len(inp):
        if inp[i] == inp[i+1]:
            j = inp[i] + inp[i+1]
            break
        else:
            pass
        i += 1
    return j

def deCoderII(j):
    A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','s','y','z']
    k = j[0]
    total = 0
    lenA = 0
    for i in A:
        if i!= k:
            lenA += 1
        else:
            break
    return 4*((lenA)+1)  


"""
test case

hint:
a = 4
b = 8
c = 12
d = 16
.
.
.
z = 104

Enter secret code : aaec
4

Enter secret code : abcc
12


Enter secret code : free
20

"""


inp = input("Enter secret code : ")    
print(deCoderII(deCoder(inp)))