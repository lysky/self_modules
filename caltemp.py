# -*- coding: utf-8 -*-

import numpy as np
import basic
def calOutlier(numList):
    def outler(num, subList):
        List = subList[:]
        aver = np.average(List)
        SD = np.std(List)
        if abs(aver - num) <= 3*SD:
            List.append(num)
        return List

    numList = basic.removeZero(numList)
    L = len(numList)
    if L <= 3:
        return numList
    elif L == 4:
        a1 = outler(numList[0], numList[1:])
        a2 = outler(numList[3], numList[:3])
        return list(set.intersection(set(a1), set(a2)))
    else:
        if L < 7:
            C = int(L/2)
            if L%2: # like 5
                subList = numList[C-1:C+2]
                R1 = range(0, C-1)[::-1]
            else: # like 6
                subList = numList[C-2:C+2]
                R1 = range(0, C-2)[::-1]
            R2 = range(C+2, L)
        else:
            C = int(L/2)
            if L%2: # like 7
                subList = numList[C-2:C+3]
                R1 = range(0, C-2)[::-1]
            else: # like 8
                subList = numList[C-3:C+3]
                R1 = range(0, C-3)[::-1]
            R2 = range(C+3, L)
        R = []
        for i in xrange(len(R1)):
            R.append(numList[R1[i]])
            R.append(numList[R2[i]])
        for r in R:
            subList = outler(r, subList)
        return subList