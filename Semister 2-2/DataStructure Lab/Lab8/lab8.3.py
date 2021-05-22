def somethingDrome(arr):
    if all(arr[i] == arr[i+1] for i in range(len(arr)-1)):
        return "Repdrome"
    elif all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    return "Plaindrome"
        return "Metadrome"
    elif all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    return "Nialpdrome"
        return "Katadrome"
    else:
        return "Nondrome"



inp = [int(a) for a in input('Enter Input : ')]
print(somethingDrome(inp))
