def sumFive(lis):
    lsAll = []
    target = 5
    absCheck = []
    count = 0
    countForDup = 0
    isAllsame = False
    if len(lis) >= 3: 
        for i in lis:
            i = abs(i)
            absCheck.append(i)
        for i in absCheck:
            for j in absCheck[1:-1]:
                    if i == j and countForDup < len(absCheck):
                        countForDup += 1
                    elif countForDup == len(absCheck):
                        break
                    else:
                        pass
                
        if countForDup == len(absCheck):
            isAllsame = True
        else:
            pass            
        if isAllsame is False:        
            for i in lis:
                for j in lis:
                    lsSum = []
                    if i != j:
                        temp = i + j
                        div = target - temp
                        if div in lis:
                            lsSum.append(i)
                            lsSum.append(j)
                            lsSum.append(div)
                            dupCheckSum = set(lsSum)
                            conTainedDupSum = len(lsSum) != len(dupCheckSum)
                            if len(lsAll) < 2:
                                if count == 1 and conTainedDupSum is True:
                                    pass
                                else:
                                    lsAll.append(lsSum)
                                    count += 1
                            else:
                                pass    
                        else:
                            pass
                    else:
                        pass
            if lsAll[0][1] in lsAll[1]:
                return "[{}]".format(lsAll[0])    
            if len(lsAll) > 0:
                return lsAll
            else:
                return 0
        else:
            for i in lis:
                for j in lis:
                    lsSum = []
                    if i != j:
                        temp = i + j
                        div = target - temp
                        if div in lis:
                            lsSum.append(i)
                            lsSum.append(j)
                            lsSum.append(div)
                            if len(lsAll) == 0:
                                lsSum[0],lsSum[1] = lsSum[1],lsSum[0]
                                lsAll.append(lsSum)
                                break
                            else:
                                pass    
                        else:
                            pass
                    else:
                        pass     
            if len(lsAll) > 0:
                return lsAll
            else:
                return 0
    else:
        return("Array Input Length Must More Than 2")                                                       

            

inp = list(map(int, input("Enter Your List : ").split()))
print(sumFive(inp))
