
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:55:47 2023

@author: saubhik
"""
#%%
# What is the output of the following code:
#immutable objects are generally passed by values
#mumatable objects are generally passed by reference
#lists are mutable and tuples are immutable
def add_items(x,y):
    x+=[1,2] #+= is nothing adding with itself x+=1 is same as x=x+1
    y+=(3,4)
l=[0]
t=(5,)
add_items(l,t)
print(l,end='')
print(t)
'''
 [0,1,2] (5,3,4)
 [0,1,2] (5,) this is the correct answer
 [0] (5,3,4)
 [0] (5,)
'''    
#%%
'''
Take an input N as an integer and write a program to display a 
right angle triangle with N rows and N columns.

Input
5

Output
* 
* * 
* * * 
* * * * 
* * * * *
'''
num=int(input('pl tell a positive integar: '))
for i in range(1,num+1):
    print(i*'*')

#%%
'''
Write a program to take an input N and print Fibonacci sequence till 
N terms.

The Fibonacci sequence is a set of integers (the Fibonacci numbers) 
that starts with a zero, followed by a one, then by another one, and 
then by a series of steadily increasing numbers. The sequence 
follows the rule that each number is equal to the sum of the 
preceding two numbers.

Input
7

Output
0
1
1
2
3
5
8

Explanation: since the input is 7 there are seven terms. The first 
two terms are always 0 and 1. The third term is sum of first two 
terms. The fourth term is sum of second and third terms and so on.
'''
def fib(n):
    ans=[0,1]
    if n<0:
        print("Invalid input")
        return
    if n==0:
        return [0]
    elif n==1:
        return [ans]
    else:
        for i in range(2,n):
            ans.append((ans[i-1]+ans[i-2]))
        return ans
ans=(fib(1))
for j in ans:
    print(j)



#%%
'''
Take base B and height H as an input and write a program to print a
 parallelogram.

Input
8
4

Output
********
********
********
********
'''
B=int(input('base'))
H=int(input('height'))
for i in range(1,H+1):
    print('*'*B)
#%%
def func(list1):
    while (len(list1)>2):
        k=list1[0]
        for i in list1:
            if k<i:
                k=i
        list1.remove(k)
        print(len(list1))
        j=list1[0]
        for i in list1:
            if j>i:
                j=i
        list1.remove(j)
        print(len(list1))
    return list1

list2=func([1,4,3,6,5,3,7,8,9,4])

print(sum(list2)/len(list2))

#%%
#local variable and global variable
#order of variable assignment
#default values
ans=0
x=3
y=9
def summation(x=1,y=2):
    ans=x/y
    return ans
print(summation(y=y,x=x))

#list are mutable object
#tuples immutable objects
#immutable objects are generally passed by values
#mumatable objects are generally passed by reference

a='saubhik'
b=a
b+='hello'
print(b)
print(a)

x=[1,2,3,5]
y=x[:]
y+=[10003]
print(y)
print(x)





















