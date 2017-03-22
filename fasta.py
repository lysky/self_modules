# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:51:43 2013
read fasta file, return dic
@author: corin li
"""
from __future__ import division
import basic

def fasta2Dic(path, fileName, shortName = 1):
    lines = basic.myFileReadlines(path, fileName)
    recDic = {}
    if shortName:
        items = lines[0][:-1].split(' ')
        gene = items[0][1:]#for the first line
    else:
        gene = lines[0][1:-1]
    seq = []
    for line in lines[1:]:
        if line[0] == '>':
            recDic[gene] = ''.join(seq)
            seq = []#save the last record
            if shortName:
                items = line[:-1].split(' ')
                gene = items[0][1:]
            else:
                gene = line[1:-1]
        else:
            seq.append(line[:-1])
    recDic[gene] = ''.join(seq)#for the last record
    return recDic
