def weirdSubtract(n,k):
    dec = ['1','2','3','4','5','6','7','8','9']
    while int(k) != 0:
        n = str(n)
        if n[-1] == '0':
            n = n[0:-1]
            k = int(k) - 1
            if k == 0:
                break
        else:
            for i in dec:
                n = str(n)
                if len(n) > 2:
                    n = str(n)
                    if n[-1] == i:
                        n = int(n)-int(i)
                        k = int(k) - int(i)
                        if k == 0:
                            break
                    elif n[-1] == '0':
                        n = n[0:-1]
                        k = int(k) - 1
                        if k == 0:
                            break
                    else:
                        pass
                else:
                    n = str(n)
                    if n[-1] == '0':
                        n = n[0:-1]
                        k = int(k) - 1
                    else:
                        n = int(n) - int(k)
                        k = int(k) - int(k)
                        break
    if int(n) > 0:
        return n
    else:
        return "0"                              
                
"""
test case

Enter num and sub : 45 26
19

Enter num and sub : 70 52
0


Enter num and sub : 14 3
11

Enter num and sub : 70 1
7

"""

n,s = input("Enter num and sub : ").split()
print(weirdSubtract(n,s))
