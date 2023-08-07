# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:30:01 2023

@author: saubh
"""

L = [[1,2,3],[0,4,5],[0,0,6]]
for i in range(3):
    for j in range(2,i-1,-1):
        print(L[i][j], end=',')
