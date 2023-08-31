# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:03:06 2023

@author: Saubhik
"""

#%%
'''
Write a Python function that takes a string s as input and returns the 
length of the largest streak of 0s in the string. For example, if the 
input string is "10001000110000000001", the function should return 9.

Input 

The input string s is guaranteed to contain only 0s and 1s.

Output

The function should return an integer, representing the length of the 
largest streak of 0s in the input string.
Your program should also print the result.

Sample output

largest_zero_streak("10101010") => 1
largest_zero_streak("10000010001") => 5
largest_zero_streak("1111") => 0
largest_zero_streak("0000") => 4
largest_zero_streak("00000000001111111111") => 10
'''
string='00000000001111111111'

def streak(s):
    if s.count('0')==len(s):
        return len(s)
    largest_streak=0
    zeros=0
    for i in s:
        if i=='0':
            zeros+=1
        else:
            if zeros>largest_streak:
                largest_streak=zeros
            zeros=0
    return largest_streak

print(streak(string))


#%%
"""
Write a Python program that calculates the dot product of two lists 
containing the same number of elements. The program should take two 
lists of integers as input from the user, and then call a function named 
dot_product to find the dot product of the two lists. The dot_product 
function should take two lists a and b as input, and should return the dot 
product of those two lists.

Your program should first prompt the user to enter the two lists of integers, 
which should be entered as strings separated by spaces. Your program should 
then convert the input strings into lists of integers. Your program should 
then call the dot_product function with the two lists as arguments, and store 
the resulting dot product in a variable named result. Finally, your program 
should print out the dot product of the two lists as the output.

You can assume that the two input lists will always contain the same number 
of elements. Your program should output an error message and exit gracefully 
if the two lists have different lengths.

In your implementation, you should define the dot_product function using a 
loop to calculate the dot product of the two input lists.
"""
a=input('You list 1 elements seperated by spaces')
b=input('You list 2 elements seperated by spaces')

def dot_product(a,b):
    a=a.split(' ')
    b=b.split(' ')
    
    # if len(a)!=len(b):
    #     return ("Error: Lists must of same size")
    result=0
    for i in range(len(a)):
        try:
            result+=int(a[i])*int(b[i])
        except Exception:
            return 'Only spaces are allowed'
        except IndexError as e:
            return e

    return result 

print(dot_product(a, b))



#%%
'''
write a Python program that finds the Greatest Common Divisor (GCD) of two 
numbers. Your program should take two input numbers from the user, and use a 
function named 'gcd' to find the GCD of those two numbers. Your program 
should then print out the GCD of the two numbers as the output.
'''
n1=int(input())
n2= int(input())

def gcd(n1,n2):
    factors=[]
    minimum=min(n1,n2)
    for i in range(1,minimum +1):
        if n1%i==0 and n2%i==0:
            factors.append(i)
            
    return max(factors)

print(gcd(n1,n2))














