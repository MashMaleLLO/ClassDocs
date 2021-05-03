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



