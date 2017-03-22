# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:07:16 2012
class of fasta
@author: corin li
"""
def rev_comp(seq_str):
#用来取反补
    transTable={"A":"T","T":"A","C":"G","G":"C","N":"N","n":"N"}
    rev_str=seq_str[::-1]
    comp_list=[]
    for i in rev_str:
        comp_list.append(transTable[i])
    return "".join(comp_list)

class fasta:
    def __init__(self, inputDir, inputName):
        self.inputDir=inputDir
        self.inputName=inputName
        self.lines=[]
        self.File=""

    def readlines(self):
        temp=open(self.inputDir+"\\"+self.inputName,"r")
        self.lines=temp.readlines()
        temp.close()
        self.lineNo=0
        for i in self.lines:
            if i[0]==">":
                break
            else:
                self.lineNo+=1
    
    def readfile(self):
        temp=open(self.inputDir+"\\"+self.inputName,"r")
        content=temp.read()
        temp.close()
        self.File=content[content.find(">"):]
        
    def seqDic(self):
        if self.lines==[]:
            self.readlines()
        sequenceDic={}
        for i in self.lines[self.lineNo:]:
            if i[0]==">":
                temp=i[:-1]
            else:
                if temp not in sequenceDic:
                    sequenceDic[temp]=[]
                    sequenceDic[temp].append(i[:-1])
                else:
                    sequenceDic[temp].append(i[:-1])
        for i in sequenceDic:
            sequenceDic[i]="".join(sequenceDic[i])
        return sequenceDic
        
    def seqList(self):
        if self.File=="":
            self.readfile()
        sequenceList=[]
        tempList=self.File.split(">")
        for i in tempList[1:]:
            lines=i.split("\n")
            sequenceList.append((">"+lines[0],"".join(lines[1:])))
        return sequenceList
        
    def selfCheck(self):
        if self.lines==[]:
            self.readlines()
        a=1
        checkDic={}
        errorList=[]
        for i in self.lines[self.lineNo:]:
            if i[0]==">":
                checkDic[i]=a
                temp=i
            else:
                checkDic[temp]+=-a
        for i in checkDic:
            if checkDic[i]==1:
                a=False
                errorList.append(i)
            else:
                a=True
        return (a,errorList)
        
            

