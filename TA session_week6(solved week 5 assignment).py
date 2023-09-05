# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:08:39 2023

@author: saubh
"""


#%%

'''
You are given a string S. Write a function count_letters which will return 
a dictionary containing letters (including special character) in string S 
as keys and their count in string S as values.

(input and output will be handled by us you just need to write the function 
 and return the dictionary)

Input
The Joy of computing

Output
{'T': 1, 'h': 1, 'e': 1, ' ': 3, 'j': 1, 'o': 3, 'y': 1, 'f': 1, 'c': 1, 
 'm': 1, 'p': 1, 'u': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1}

Explanation: T is appeared once in the string, similarly o is appeared 3 
times in the string and so on. (You do not have to worry about the order of 
arrangement in your dictionary)
'''


def count_letters(s):
    counted={}
    
    for i in s:
        try:
            counted[i]+=1
        except KeyError:
            counted[i]=1
    return counted
a='banana'
print(count_letters(a))

#%%
'''
You are given a list L. Write a function uniqueE which will return a list 
of unique elements is the list L in sorted order. (Unique element means it 
should appear in list L only once.)

Input will be handled by us

Input
[1,2,3,3,4,4,2,5,6,7]

Output
[1,5,6,7]

Explanation

Elements 1,5,6,7 appears in the input list only once.
'''

def uniqueE(L):
    # uniqs=[]
    # for i in L:
    #     if L.count(i)==1:
    #         uniqs.append(i)
    return sorted([i for i in L if L.count(i)==1 ])
    
print(uniqueE([1,2,3,3,4,4,2,5,6,7]))

#%%
'''
You are given a list L. Write a program to print first prime number 
encountered in the list L.(Treat numbers below and equal to 1 as non prime)

Input will be handled by us.

Input
[1,2,3,4,5,6,7,8,9]

output
2

Explanation
Since 2 is the first prime number is list L, therefor it is printed.
'''

def fst_prime(L):
    for i in L:
        if i==2:
            return i
        elif i>2:
            for j in range(2,i):
                if i%j==0:
                    break
                elif j==i-1:
                    return i
                
print(fst_prime([int(i) for i in '70 -3 182 47 180 266 -91 -101 -75 280 -67 42 -142 -141 -82 296 -69 144 -80 116 -97 140 38 81 -40 37 251 -120 54 90'.split()]))            
                