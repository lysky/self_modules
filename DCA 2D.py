# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:28:23 2013

@author: corin li
"""
from __future__ import division
import matplotlib.pyplot as plt
import basic
filePath = r'D:\pythontest\input'
fileName = 'DCA.txt'
#figTitle = 'AF expIdx SNR2 inorm'
figTitle = '40h xylan'
#group is the replicates
group = 1
mark = {0:'bo', 1:'yd', 2:'rx', 3:'gv', 4:'ks'}
csv = basic.readCSV(filePath, fileName)
xlabel = csv[0][1]
ylabel = csv[0][2]
name, d1, d2, d3 = [], [], [], []
for i in csv[1:]:
    name.append(i[0])
    d1.append(float(i[1]))
    d2.append(float(i[2]))
d1max = max([abs(x) for x in d1])
d2max = max([abs(x) for x in d2])
plt.subplot(111)
plt.subplots_adjust(wspace = 0.25, hspace = 0.4, right = 0.75, left  = 0.125)
for i in xrange((len(csv) -1)//group):
    start = group*i
    end = group*i + group
    plt.plot(d1[start:end], d2[start:end], mark[i], label = name[start][:-1], markersize=8)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
xlim = plt.xlim()
ylim = plt.ylim()
plt.plot(xlim,[0,0], 'k')
plt.plot([0,0], ylim, 'k')
plt.xlim(xlim)
plt.ylim(ylim)
plt.title(figTitle)


plt.show()

