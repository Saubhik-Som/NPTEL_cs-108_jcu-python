# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:10:37 2023

@author: Saubhik
"""

#%%
'''
Take 3 sides of a triangle as an input and find whether that triangle is a right angled triangle or not. Print 'YES' if a triangle is 
right angled triangle or 'NO' if it's not.

Input:
3
4
5

Output
YES
'''
data=input()
triangle=[]
while data:
    triangle.append(float(data))
    data=input()

def right_angle_triangle(triangle):
    if len(triangle)!=3:
        return "give only three sides of a triangle"
    triangle=sorted(triangle)
    if ((triangle[0])**2+(triangle[1])**2==(triangle[2])**2):
        return 'YES'
    else: return "NO"

print(right_angle_triangle(triangle))



#%%
'''
Write a program that accepts a hash-separated sequence of words as input and prints the words in a hash-separated sequence after sorting 
them alphabetically in reverse order.

Input:
hey#input#bye

Output:
input#hey#bye
'''
print(('#').join(sorted(input().split('#'),reverse=True)))


#%%
'''
Write a program which takes two integer a and b and prints all composite numbers between a and b.(both numbers are inclusive)

Input:
10
20

Output:
10
12
14
15
16
18
20
'''
def composite(n):
    for i in range(2,n):
        if n%i==0:
            return n
    return

def give_composites():
    n1=int(input())
    n2=int(input())
    for n in range(min(n1,n2),max(n1,n2)+1):
        if composite(n)!=None:
            print(n)

give_composites()

#%%
'''
Write a program to an integer as an input and reverse that integer.

Input:
A single integer.

Output:
Reverse number of that integer.

Example:

Input:
54321

Output:
12345
'''

print(int(input()[::-1]), end='')


#%%
'''
Given a list of strings, write a program to write sort the list of strings on the basis of last character of each string.

Input:
L = ['ram', 'shyam', 'laksham']

Output:
['laksham', 'ram', 'shyam']
'''
L=input().split(' ')
def function(L):
  new_L=[i[::-1] for i in L]
  new_L=sorted(new_L)
  return ([i[::-1] for i in new_L])

print(function(L),end='')



#%%
'''
Given a student's roll number in the following format rollNumber@institute.edu.in, write a program to find the roll number and institute name of the student.

Input:
roll@institute.edu.in

Output:
roll institute
'''

'''
[roll,institute.edu.in]
[institute, edu, in]
'''
s=input()
print(s.split('@')[0]+' '+s.split('@')[1].split('.')[0], end='')





