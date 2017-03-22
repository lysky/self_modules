# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:28:23 2013

@author: corin li
"""
from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import basic
filePath = r'D:\pythontest\input'
fileName = 'DCA.txt'
figTitle = 'AF expIdx SNR2 inorm'
#figTitle = 'AF from pipeline'
group = 1
mark = {0:'bo', 1:'yd', 2:'rx', 3:'gv', 4:'ks'}
csv = basic.readCSV(filePath, fileName)
name, d1, d2, d3 = [], [], [], []
for i in csv[1:]:
    name.append(i[0])
    d1.append(float(i[1]))
    d2.append(float(i[2]))
    d3.append(float(i[3]))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#plt.subplots_adjust(wspace = 0.25, hspace = 0.4, right = 0.75, left  = 0.125)
for i in xrange((len(csv) -1)//group):
    start = group*i
    end = group*i + group
    ax.scatter(d1[start:end], d2[start:end], d3[start:end], c = mark[i][0], marker = mark[i][1], s = 30)
#    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    ax.set_xlabel(csv[0][1])
    ax.set_ylabel(csv[0][2])
    ax.set_zlabel(csv[0][3])
plt.title(figTitle)


plt.show()

