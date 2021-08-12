def coolRanged(*args):
    count = len(args)
    ls = []
    if count == 1:
        i = 0.0
        stopped = args[0]
        while i < stopped:
            ls.append(round(i, 3))
            i += 1
        return tuple(ls)    
    elif count == 2:
        stopped = args[1]
        started = args[0]
        i = started
        while i < stopped:
            ls.append(round(i, 3))
            i += 1
        return tuple(ls)  
    else:
        stopped = args[1]
        started = args[0]
        steped = args[2]
        i = started
        while i < stopped:
            ls.append(round(i, 3))
            i += steped
        return tuple(ls)    
            

"""
test case

*** New Range ***
Enter Input : 1 10 1
(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)

*** New Range ***
Enter Input : 2 20 1.3
(2.0, 3.3, 4.6, 5.9, 7.2, 8.5, 9.8, 11.1, 12.4, 13.7, 15.0, 16.3, 17.6, 18.9)


*** New Range ***
Enter Input : 1 20 5.3
(1.0, 6.3, 11.6, 16.9)

"""



if __name__ == "__main__":
    print("*** New Range ***")
    inp = [inp for inp in input("Enter Input : ").split()]
    l = len(inp)
    if l == 1:
        num = int(inp[0])
        print(coolRanged(num))
    elif l == 2:
        started = float(inp[0])
        stopped = float(inp[1])
        print(coolRanged(started,stopped))
    else:
        started =float(inp[0])
        stopped = float(inp[1])
        steped = float(inp[2])
        print(coolRanged(started,stopped,steped))       



