l = []
def reversedlist(lst):
    global l
    if lst == []:
        return 
    else:
        t = lst.index(max(lst))
        j = lst.pop(t)
        l.append(j)
        return reversedlist(lst)

inp = input("Enter your List : ").split(',')
lk = []
for i in inp:
    i = int(i)
    lk.append(i)
reversedlist(lk)
print("List after Sorted : {}".format(l))
