# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:20:42 2023

@author: saubhik
"""

#%%
'''
Write a program that takes a number `n` as input and prints the sum of the 
squares of the first `n` positive integers.

Example:

If n = 4, the program should output 30 (1^2 + 2^2 + 3^2 + 4^2) = 30
'''
n=int(input('provide a positve integer:'))
ans=0
for i in range(1,n+1):
    ans+=i**2
print(ans)

#%%
'''
Write a program that takes a number `n` as input and prints the nth power of 2.

Example:
If n = 4, the program should output 16 (2^4 = 16)
'''
n=float(input('provide a number:'))
ans=2**n
print(ans)

#%%
'''
Write a program that takes a number `n` as input and prints a pyramid of 
numbers with `n` rows.

Example:

If n = 5, the program should output the following
 	1
   232
  34543
 4567654
567898765
If n = 10, the program should output the following
         1
        232
       34543
      4567654
     567898765
    67890109876
   7890123210987
  890123454321098
 90123456765432109
10123456789876543210
'''
def pyramid_builder(n):
    for row in range(1,n+1):
        #print the leading spaces
        print(' '*(n-row), end='')
        
        num=row #initiate num with row number
        
        #print the increasing numbers
        for j in range(row):
            print(num, end='')
            num=(num+1)%10
        
        num=(num-2)%10 #decresing num variable to the first element of the decreasing nums
        
        #prining the decreasing numbers
        for k in range(row-1):
            print(num, end='')
            num=(num-1)%10
        print()
        

pyramid_builder(16)
        
#%%
L1=['harry potter', 'matrix', 'spiderman', 'avengers', 'john wick' ]
L2=['drishyam', 'spiderman', 'bahubali', 'dhoom', 'race', 'matrix']

L=[]

for i in range(len(L1)):
    
    flag= 0
    
    for j in range(len(L2)):
        
        if L1[i] == L2[j]:
            flag= 1
            break
        else:
            flag=0
    if flag==0:
        L.append(L1[i])
print(L)

'''
 Print unique movies of list L1
 Print unique movies of list L2
 Print unique movies of list L1 and L2
 Shows an error
'''

#%%
'''
A perfect number is a positive integer that is equal to the sum of its 
positive divisors, excluding the number itself. For example, 6 is a perfect 
number as the sum of its divisors 1,2,3 is equal to 6.
Write a function which will return True if the number is a perfect number?
'''

def perfect_num(n):
    #divisors=[]
    divisors=0
    for i in range(1,n):
        if n%i==0:
            #divisors.append(i)
            divisors+=i
    #if sum(divisors)==n:
    if divisors==n:
        return True
    else: 
        return False

print(perfect_num(6))
    

















