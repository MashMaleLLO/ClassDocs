
"""
Testcase

Enter All Bid : 10 20 1 2 5
winner bid is 20 need to pay 10

"""

bit = [int(inp) for inp in input("Enter All Bid : ").split()]
count = 0
Highest = 0
SecondHightest = 0
error = False

if len(bit) == 1:
    print("not enough bidder")
else:
    pass

Highest = max(bit)

for i in bit:
    
    if int(i) == int(Highest):
        count += 1
    else:
        pass

if count > 1:
    print("error : have more than one highest bid")
else:
    if len(bit) > 1:
        bit.remove(Highest)
    else:
        pass    
    SecondHightest = max(bit)
    if len(bit) > 1:
        print("winner bid is {} need to pay {}".format(Highest, SecondHightest))
    else:
        pass

        
       