# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 00:41:47 2012
method related to microarray
isolate raw data; translate geneid to sequenceNo;
@author: corin li
"""
import basic
import os
import numpy as np
import copy

class rawSig:
    def __init__(self, filePath, fileName):
        self.lines = basic.myFileReadlines(filePath, fileName)
        self.rawDic = {}        
        for line in self.lines[1:]:
            self.rawDic[line[:9]] = line[10:-1]
    def getRawDic(self):
        '''return the dic senquenceNo -> tab separated raw data'''
        return self.rawDic
    def getData(self, sequenceList):
        '''get the data of the sequence in the sequenceList formated'''
        result = [self.lines[0]]
        blank = self.lines[0].count('\t')-1
        for seq in sequenceList:
            try:
                result.append(seq + '\t' + self.rawDic[seq] + '\n')
            except:
                result.append(seq + '\t' + '\t'*blank + '\n')
        return ''.join(result)
    def record2value(self, string):
        '''seqarate the record to the set of triplicate and change to float'''
        value = []
        items = string.split('\t')
        for i in range(len(items)//3):
            replicate = []
            for n in range(3):
                try:
                    replicate.append(float(items[n+3*i]))
                except:
                    replicate.append(0)
            value.append(replicate)
        return value

def transToSequenceNo(inputDir, translationTable):
    """
    need import basic; translate geneID in microarray to sequenceNo
    """
    IDDic = {}
    fileTemp=basic.myFile(inputDir,translationTable)
    lines = fileTemp.readFile()
    for line in lines:
        IDList = line.split("\t")
        IDDic[IDList[0]] = IDList[1][:-1]
    return IDDic

def transSeqNotoGeneID(inputDir,translationTable):
    """
    need import basic; translate SeuqenceNo to in microarray geneID
    """
    IDDic = {}
    fileTemp=basic.myFile(inputDir,translationTable)
    lines = fileTemp.readFile()
    for line in lines:
        IDList = line.split("\t")
        IDDic[IDList[1][:-1]] = IDList[0]
    return IDDic

def isolateRawWithTime (inputDir):
    """
    isolate the raw data from a folder, return 5 dict, with key as the geneID, and list of 3 raw
    data as the value. The name of raw data must be as "raw data AF 60h vs 40h.txt"
    """
    #summarize according to different experiment set
    fileNames=os.listdir(inputDir)
    control=1
    names={}
    for idx, fileName in enumerate(fileNames):
        fileTemp=basic.myFile(inputDir,fileName)
        lines=fileTemp.readFile()
        controlTemp=[]
        #create variance to store the result of the input file
        names["dic%s" %fileName[12:15]]={}
        #separate genes with control
        genes=(len(lines)-1)//3
        resultTemp={}
        treatmentTemp=[]
        for i in xrange(genes):
            if lines[1+i*3][:4]=="gene":
                #record the result of control
                if control:
                    #MicroarrayID+the following result line
                    controlTemp.append(lines[1+i*3][:-1]+lines[2+i*3])
                treatmentTemp.append(lines[1+i*3][:-1]+lines[3+i*3])
        if control:
            #break the control line to get the result data
            for item in controlTemp:
                itemTemp=item.split("\t")
                itemTemp0=itemTemp[6].split(",")
                itemTemp2=[]
                for a in itemTemp0:
                    # 3 replicate result in float format
                    itemTemp2.append(float(a))
                #resultTemp[microarrayID]=3 result data
                resultTemp[itemTemp[0]]=itemTemp2
            controlDic=resultTemp
            resultTemp={}
            #do not calculate control next time in the same data set
            control=0
        #Break other test line to get the result data
        for item in treatmentTemp:
            itemTemp=item.split("\t")
            itemTemp0=itemTemp[6].split(",")
            itemTemp2=[]
            for a in itemTemp0:
                # 3 replicate result in float format
                itemTemp2.append(float(a))
            #resultTemp[microarrayID]=3 result data
            resultTemp[itemTemp[0]]=itemTemp2
        if fileName[12:15]=="90h":
            names["dic80h"]=resultTemp
        else:
            names["dic%s" %fileName[12:15]]=resultTemp
    return [controlDic,names["dic60h"],names["dic70h"], names["dic80h"],names["dic100"]]

def isolateRaw (inputdir):
    """
    return a list of dic without dic name
    """
    fileNames=os.listdir(inputdir)
    control=1
    names={}
    result = []
    for indx,fileName in enumerate(fileNames):
        fileTemp=basic.myFile(inputdir,fileName)
        lines=fileTemp.readFile()
        controlTemp=[]
        names["dic%s" %indx]={}
        genes=(len(lines)-1)//3
        resultTemp={}
        treatmentTemp=[]
        for i in xrange(genes):
            if lines[1+i*3][:4]=="gene":
                if control:
                    controlTemp.append(lines[1+i*3][:-1]+lines[2+i*3])
                treatmentTemp.append(lines[1+i*3][:-1]+lines[3+i*3])
        if control:
            for item in controlTemp:
                itemTemp=item.split("\t")
                itemTemp0=itemTemp[6].split(",")
                itemTemp2=[]
                for a in itemTemp0:
                    itemTemp2.append(float(a))
                resultTemp[itemTemp[0]]=itemTemp2
            names["controlDic"]=resultTemp
            resultTemp={}
            control=0
        for item in treatmentTemp:
            itemTemp=item.split("\t")
            itemTemp0=itemTemp[6].split(",")
            itemTemp2=[]
            for a in itemTemp0:
                itemTemp2.append(float(a))
            resultTemp[itemTemp[0]]=itemTemp2
    names["dic%s" %indx]=resultTemp
    dicList = names.items()
    for i in range(len(names)):
        result.append(dicList[i][1])
    return result   

def noZeroAverage(numList, notChangeList = True):
    if notChangeList:
        numList = copy.copy(numList)
    if 0 in numList:
        numList.remove(0)
    return np.average(numList)