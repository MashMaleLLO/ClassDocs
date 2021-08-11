
"""
Testcase

 ***Function Odd List***
Enter list numbers : 1 2 3 4 5 6 7 8 9
Input list :  [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Output list :  [1, 3, 5, 7, 9]

"""



def odd_list(al):
    ls = []
    for i in al:
        if i%2 != 0:
            ls.append(i)
        else:
            pass
    return ls   
           



if __name__ == "__main__":
    print(" ***Function Odd List***")
    ls = [int(e) for e in input("Enter list numbers : ").split()]
    opls = odd_list(ls)
    print("Input list : ", ls, "\nOutput list : ", opls)

        