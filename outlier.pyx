def calOutlier(list numList):
#    numList = removeZero(numList)
    if type(numList[0]) is tuple:
        numList.sort(key = lambda x:x[1])
        outlier = outlierTuple
    else:
        numList.sort()
        outlier = outlierNum
    cdef list subList, R1, R2, a1, a2, R
    cdef int C, LR1
    cdef int L = int(len(numList))
    if L <= 3:
        return numList
    elif L == 4:
        a1 = outlier(numList[0], numList[1:])
        a2 = outlier(numList[3], numList[:3])
        if len(a1) > len(a2):
            return a2
        else:
            return a1
    else:
        if L < 7:
            C = L//2
            if L%2: # like 5
                subList = numList[C-1:C+2]
                R1 = range(0, C-1)[::-1]
            else: # like 6
                subList = numList[C-2:C+2]
                R1 = range(0, C-2)[::-1]
            R2 = range(C+2, L)
        else:
            C = L//2
            if L%2: # like 7
                subList = numList[C-2:C+3]
                R1 = range(0, C-2)[::-1]
            else: # like 8
                subList = numList[C-3:C+3]
                R1 = range(0, C-3)[::-1]
            R2 = range(C+3, L)
        R = []
        LR1 = int(len(R1))
        for i in range(LR1):
            R.append(numList[R1[i]])
            R.append(numList[R2[i]])
        for r in R:
            subList = outlier(r, subList)
        return subList

cpdef inline object outlierNum(double num, list subList):
    cdef list List = subList[:]
    cdef double aver, SD
    aver, SD = meanstdp(subList)
    if abs(aver - num) <= 3*SD:
        List.append(num)
    return List

cpdef inline object outlierTuple(tuple num, list subList):
    cdef list List = subList[:]
    cdef tuple x
    cdef list VList = [x[1] for x in subList]
    cdef double aver, SD
    aver, SD = meanstdp(VList)
    if abs(aver - num[1]) <= 3*SD:
        List.append(num)
    return List

cpdef inline tuple meanstdp(list x):
    cdef double n = float(len(x))
    cdef double mean = 0, std = 0
    cdef double a
    for a in x:
        mean += a
    mean = mean / n
    for a in x:
        std += (a - mean)**2
    std = (std / n)**0.5
    return (mean, std)

cpdef inline tuple meanstds(list x):
    cdef double n = float(len(x))
    cdef double mean = 0, std = 0
    cdef double a
    for a in x:
        mean += a
    mean = mean / n
    for a in x:
        std += (a - mean)**2
    std = (std / (n-1))**0.5
    return (mean, std)

cpdef list removeZero(list numList):
    '''For only positive numbers'''
    numList.sort()
    cdef int count = 0
    cdef double i
    for i in numList:
        if i == 0:
            count += 1
        else:
            break
    return numList[count:]