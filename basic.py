# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:44:04 2012

@author: corin li
"""
import cPickle as cP
import os
import csv

class myFile:
    def __init__(self,fileDir, fileName):
        self.dir=fileDir
        self.name=fileName
    def readFile(self):
        temp=open(self.dir+"\\"+self.name,"r")
        lines=temp.readlines()
        temp.close()
        return lines
    def writeFile(self,result):
        temp=open(self.dir+"\\"+self.name,"w")
        temp.write(result)
        if result[:-1] != '\n':
            temp.write('\n')
        temp.close()
    def appendFile(self,result):
        temp=open(self.dir+"\\"+self.name,"a")
        temp.write(result)
        if result[:-1] != '\n':
            temp.write('\n')
        temp.close()

def myFileReadlines(fileDir, fileName):
    fileTemp = myFile(fileDir, fileName)
    return fileTemp.readFile()

def readLines(fileDir, fileName):
    '''Same as myFileReadlines'''
    fileTemp = myFile(fileDir, fileName)
    return fileTemp.readFile()

def myFileWriteFile(fileDir, fileName, result):
    '''Automatically add '\n' at the end'''
    fileTemp = myFile(fileDir, fileName)
    fileTemp.writeFile(result)

def writeFile(fileDir, fileName, result):
    '''Same as myFileWriteFile. Automatically add '\n' at the end'''
    fileTemp = myFile(fileDir, fileName)
    fileTemp.writeFile(result)

def writeCSV(fileDir, fileName, result):
    output = open(fileDir+'\\'+fileName, 'wb')
    writer = csv.writer(output, dialect = 'excel-tab')
    writer.writerows(result)
    output.close()
def readCSV(fileDir, fileName, withTitle = False):
    '''Return a multilist of the table, if withTitle = True, title will be the fisrt element of the list'''
    reader = csv.reader(open(fileDir+'\\'+fileName, 'rb'), dialect = 'excel-tab')
    if withTitle:
        temp = list(reader)
        return temp[1:]
    else:
        return list(reader)

def dump(out_Dir, out_name, anything):
    """
    dump anything as out_name to out_dir
    """
    f = open(out_Dir+"\\"+ out_name,"wb")
    cP.dump(anything,f,2)
    f.close()

def load(out_Dir, out_name):
    """
    load out_name from out_Dir to anything then return anything
    """
    f = open(out_Dir+"\\"+ out_name, 'rb')
    anything = cP.load(f)
    f.close()
    return anything

def combineKeys(dicList, value):
    """
    combine all the keys and return an dict. The keys are the combined keys. The value of the dict is the gaven value when define the function.
    """
    dicTemp = {}
    if value == []:
        for dic in dicList:
            for key in dic:
                dicTemp[key] = []
    elif value == {}:
        for dic in dicList:
            for key in dic:
                dicTemp[key] = {}
    else:
        for dic in dicList:
            for key in dic:
                dicTemp[key] = value
    return dicTemp

def getFileNameInFolder(folder, outputPath, outputName):
    '''Write the fileName in a folder to outputPath'''
    fileNames = os.listdir(folder)
    myFileWriteFile(outputPath, outputName, '\n'.join(fileNames)+'\n')

def D2ListToFile(D2List, fileName, filePath = None):
    '''Save 2D list to file'''
    if filePath == None:
        filePath = os.getcwd()
    tempList = []
    for i in D2List:
        tempList.append('\t'.join((str(x) for x in i)))
    myFileWriteFile(filePath, fileName, '\n'.join((x for x in tempList)) + '\n')

# ---------- code for class: curry (begin)
class curry:
    """from Scott David Daniels'recipe
    "curry -- associating parameters with a function"
    in the "Python Cookbook"
    http://aspn.activestate.com/ASPN/Python/Cookbook/
    """

    def __init__(self, fun, *args, **kwargs):
        self.fun = fun
        self.pending = args[:]
        self.kwargs = kwargs.copy()

    def __call__(self, *args, **kwargs):
        if kwargs and self.kwargs:
            kw = self.kwargs.copy()
            kw.update(kwargs)
        else:
            kw = kwargs or self.kwargs
        return self.fun(*(self.pending + args), **kw)
# ---------- code for class: curry (end)


# ---------- code for function: event_lambda (begin)
def event_lambda(f, *args, **kwds ):
    """A helper function that wraps lambda in a prettier interface.
    Thanks to Chad Netzer for the code."""
    return lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )

def removeZero(numList):
    '''For only positive numbers'''
    numList.sort()
    count = 0
    for i in numList:
        if i == 0:
            count += 1
        else:
            break
    return numList[count:]

def sub_lists(List, n=4, groups = True):
    '''if groups is True, lis with be sub into 4 group, else it will be sub by step 4'''
    if groups:
        sub_into = n
        step = len(List) // sub_into
        left = len(List) % sub_into
        if left == 0:
#            for i in xrange(0, len(List), step):
#                yield List[i:i+step]
            return [List[i:i+step] for i in xrange(0, len(List), step)]
        else:
            adjust = [left] * (sub_into + 1)
            for i in xrange(left):
                adjust[i] = i
            tempPosition = range(0, len(List), step)
            position = [tempPosition[i] + adjust[i] for i in range(len(adjust))]
#            for i in xrange(len(position) -1 ):
#                yield List[position[i]:position[i+1]]
            return [List[position[i]:position[i+1]] for i in xrange(len(position) -1 )]
    else:
        return [List[i:i+n] for i in xrange(0, len(List), n)]

def cache(function):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper
def transpose(multiList):
    c = len(multiList[0])
    return [[L[i] for L in multiList] for i in xrange(c)]

def file2Dic(path, fileName, key = 0, start = 1, end = 'E'):
    '''Return (titleTuple, recordDic), pay attention to the title, it is (key, others). The recordDic is lists'''
    csv = readCSV(path, fileName)
    if end == 'E':
        end = len(csv[0])
    titleTuple = (csv[0][key], csv[0][start:end])
    recordDic = {}
    for i in csv[1:]:
        recordDic[i[key]] = i[start:end]
    return (titleTuple, recordDic)

def var_name(variable, start_globals, now_globals):
    '''get the str of the variable name, start_globals is a list of the globals names at the start point. use globals().keys()'''
    nameList = []
    s_globals = set(start_globals)
    for name in now_globals:
        if eval(name, now_globals) == variable:
            if name not in s_globals:
                nameList.append(name)
    name = ', '.join(nameList)
    if len(nameList) > 1:
        print('The varible name of\n%s\nis ambiguous, please check function var_name' %name)
        return name + ', please check function var_name'
    elif nameList == []:
        print('Did not get the variable name, please check function var_name')
        return 'check function var_name'
    else:
        return name