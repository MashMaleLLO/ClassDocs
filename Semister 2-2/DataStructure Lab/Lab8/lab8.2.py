def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

inp = [int(a) for a in input('Enter Input : ').split()]
arr = []
arr2 = {}
arr3 = {}
arr4 = {}
arr5 = {}
arr6 = {}
i = 0
while i < len(inp):
    if inp[i] < 0:
        k = {inp[i]:i}
        if inp[i] in arr2:
            if inp[i] in arr3:
                if inp[i] in arr4:
                    if inp[i] in arr5:
                        arr6.update(k)
                    else:
                        arr5.update(k)
                else:
                    arr4.update(k)
            else:
                arr3.update(k)
        else:
            arr2.update(k)
        i += 1
    else:
        arr.append(inp[i])
        i += 1
bubbleSort(arr)
for i in arr2:
    arr.insert(arr2[i],i)
for i in arr3:
    arr.insert(arr3[i],i)
for i in arr4:
    arr.insert(arr4[i],i)
for i in arr5:
    arr.insert(arr5[i],i)
for i in arr6:
    arr.insert(arr6[i],i)
strt = ""
for i in arr:
    strt += str(i) + " "
print(strt)
