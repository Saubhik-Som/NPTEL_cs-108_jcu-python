# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:57:45 2023

@author: Saubhik
"""

#%%
'''
Write a Python function frequency(l) that takes as input a list of integers 
and returns a pair of the form (minfreqlist,maxfreqlist) where

    minfreqlist is a list of numbers with minimum frequency in l, sorted in 
    ascending order
    
    maxfreqlist is a list of numbers with maximum frequency in l, sorted in 
    ascending order

[8,1,2,2,1,3,4,5,4,4,5,5,7]
minfreqlist=[3,7,8]
maxfreqlist=[4,5]
==>([3,7,8],[4,5])
'''
l=[0,0,0,0,0,]
def frequency(l):
    l=sorted(l) #sorting the input list for further processing
    #making a list of lists to get all same elements in one list
    l_seperated=[]
    same=[]
    for i in l:
        if i in same or len(same)==0:
            same.append(i)
        elif i not in same:
            l_seperated.append(same)
            same=[]
            same.append(i)
    l_seperated.append(same)
    
    #getting the min and max freq list by checking the length of the lists with same elements
    minfreqlist=[]
    maxfreqlist=[]
    for i in l_seperated:
        if len(i)==len(min(l_seperated, key=len)):
            minfreqlist.append(i[0])
        if len(i)==len(max(l_seperated, key=len)):
            maxfreqlist.append(i[0])
    return (minfreqlist,maxfreqlist)

print(frequency(l))

def new_frequency(l):
    l_seperated={}
    for i in l:
        if i in l_seperated.keys():
            l_seperated[i]+=1
        else: l_seperated[i]=1
    # minimum,maximum=min(l_seperated.values()),max(l_seperated.values())
    # minfreqlist=[]
    # maxfreqlist=[]
    # for keys in l_seperated:
    #     if l_seperated[keys]==minimum:
    #         minfreqlist.append(keys)
    #     if l_seperated[keys]==maximum:
    #         maxfreqlist.append(keys)
    minfreqlist=[keys for keys in  l_seperated if l_seperated[keys]==min(l_seperated.values())]
    maxfreqlist=[keys for keys in  l_seperated if l_seperated[keys]==max(l_seperated.values())]
    return (sorted(minfreqlist),sorted(maxfreqlist))
 
    
print(new_frequency(l))
#%%
'''
Given a sqaure matrix M, write a function DiagCalc that calculates the sum of left and right diagonals and prints it respectively.

Input:

A Number M 
A Matrix with M rows and M columns
[[1,2,3],[3,4,5],[6,7,8]] 

Output 
13
13

Explanation:
Sum of left diagonal is 1+4+8 = 13
Sum of right diagonal is 3+4+6 = 13
'''
M=[[1,2,3,9],[3,4,5,9],[6,7,8,9],[0,0,0,0]] 
def DiagCalc(M):
    left_diag=0
    right_diag=0
    for i in range(len(M)):
        left_diag+= M[i][i]
        right_diag+=M[i][len(M)-1-i]

    return [left_diag,right_diag]

for i in DiagCalc(M):
    print(i)


#%%
'''
Given a matrix M write a function Transpose which accepts a matrix M and return the transpose of M.
Transpose of a matrix is a matrix in which each row is changed to a column or vice versa.

Input 
A matrix M
[[1,2,3],[4,5,6],[7,8,9]]

Output
Transpose of M
[[1,4,7],[2,5,8],[3,6,9]]
'''

M=[[1,2,3],[4,5,6]]
def transpose(M):
    transpose_M=[[0 for i in range(len(M))] for j in range(len(M[0]))]
    
    for i in range(len(M)):
        for j in range(len(M[i])):
            transpose_M[j][i]=M[i][j]

    return transpose_M

transpose_M=transpose(M)
print(transpose_M)

import numpy as np

M=np.array(M)
transpose_M=M.transpose()
print(transpose_M)


#%%
'''
Given a matrix M write a function snake that accepts a matrix M and returns 
a list which contain elements in snake pattern of matrix M. 
(See explanation to know what is a snake pattern)

Input
A matrix M
91 59 21 63 
81 39 56 8 
28 43 61 58 
51 82 45 57

Output
[91, 59, 21, 63, 8, 56, 39, 81, 28, 43, 61, 58, 57,45,82,51]

Explanation:

For row 1 elements are inserted from left to right
For row 2 elements are inserted from right to left
For row 3 elements are inserted form left to right 
and so on
'''
M=[[91, 59, 21, 63], 
   [81, 39, 56, 8], 
   [28, 43, 61, 58], 
   [51, 82, 45, 57]]
def make_snake(M):
    snake_M=[]
    for row in range(len(M)):
        if row %2==0:
            snake_M+=[i for i in M[row]]
        else:
            snake_M+=[i for i in M[row][::-1]]
        
    return snake_M

print(make_snake(M))




#%%
"""
An airline has assigned each city that it serves a unique numeric code. It has 
collected information about all the direct flights it operates, represented 
as a list of pairs of the form (i,j), where i is the code of the starting 
city and j is the code of the destination.

It now wants to compute all pairs of cities connected by one intermediate 
hop — city i is connected to city j by one intermediate hop if there are 
direct flights of the form (i,k) and (k,j) for some other city k. The airline 
is only interested in one hop flights between different cities — pairs of the form (i,i) are not useful.

Write a Python function onehop(l) that takes as input a list of pairs 
representing direct flights, as described above, and returns a list of all 
pairs (i,j), where i != j, such that i and j are connected by one hop. Note 
that it may already be the case that there is a direct flight from i to j. 
So long as there is an intermediate k with a flight from i to k and from k 
to j, the list returned by the function should include (i,j). The input list 
may be in any order. The pairs in the output list should be in 
lexicographic (dictionary) order. Each pair should be listed exactly once.

Here are some examples of how your function should work.

 
>>> onehop([(2,3),(1,2)])
[(1, 3)]

>>> onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])
[(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

>>> onehop([(1,2),(3,4),(5,6)])
[]
"""




