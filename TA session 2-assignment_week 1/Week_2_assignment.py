# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:41:49 2023

@author: saubh
"""
#%%
'''
assignment 1
Given an integer as an input, write a program to print that integer.

Input
A number 

Output
A number
'''
num=input("Please input an interger: ",)
num=int(num)
print(num)

#%%
'''
Asignment 2
Given two integers as an input, write a program to print 
the sum of those two integers.
'''
num1 = int(input())
num2 = int(input())
print(num1+num2)

#%%
'''
You are given a number as an input. You have to display all the 
numbers from 0 till x
'''
num=int(input("Give an integer: ",))
for i in range(num+1):
    print(i)

