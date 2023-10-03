# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:13:27 2023

@author: Saubhik
"""
#%%
'''
Given two string s1 and s2, write a function subStr which accepts two 
parameters s1 and s2 and will return True if a s2 is a substring of s1 
otherwise return False. A substring is a contiguous sequence of 
characters within a string. 

Input:

bananamania
nana

Output:
True

Explanation:

S2 which is nana is in bananamania hence it is a substring of s1.

Example 2:

Input:

aabbcc


output:
False
'''
s1=input('your string: ')
s2=input('your substring: ')
def subStr(s2,s1):
    return s2 in s1

print(subStr(s2,s1))

#%%
'''
Take an integer N as an input, print all the indices of numbers in that 
integer from left to right.

Input:

122345

Output:
1 0 
2 1 2
3 3
4 4
5 5

Explanation:

Given integer 122345. Now printing indexes of numbers from left to right.
First number is 1 and its index is 0 therefore
1 0 

Second and third number is 2 and its index is 1,2 therefore
2 1 2

and so on...
'''
N=(input('write an integar:'))
def write_indx(N):
    index_dict={}
    for idx, i in enumerate(N):
        try:
            index_dict[i]+=[idx]
        except KeyError:
            index_dict[i]=[idx]
    return index_dict

res=write_indx(N)

for key in res:
    print(key,end=' ')
    val=res[key]
    for i in val:
        print(i, end=' ' )
    print()
    
         

#%%
'''
Given two dictionaries d1 and d2, write a function mergeDic that accepts two 
dictionaries d1 and d2 and return a new dictionary by merging d1 and d2. 
Note: Contents of d1 should appear before contents of d2 in the new 
dictionary and in same order. In case of duplicate value retain the value 
present in d1.

Input:
{1: 1, 2: 2}
{3: 3, 4: 4}

output:
{1: 1, 2: 2, 3: 3, 4: 4}
'''
d1={1: 1, 4: 4, 2: 2}
d2={3: 3, 1: 5}
def mergeDic(d1,d2):
    for key in d2:
        if key not in d1.keys():
            d1[key]=d2[key]
    return d1

d=mergeDic(d1, d2)







