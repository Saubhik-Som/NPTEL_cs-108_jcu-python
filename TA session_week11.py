# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:27:25 2023

@author: saubh
"""
#%%
'''
Given a list L write a program to make a new list to fix the indexes of 
numbers to in list L to its same value in the new list. Put 0 at remaining 
indexes. Also print the elements of the new list in the single line. 
(See explanation for more clarity.)

Input:
[1,5,6]

Output:
0 1 0 0 0 5 6

Explanation: 

List L contains 1,5,6 so at 1,5,6, index of new list the respective values 
are put and rest are initialized as zero.
'''
inp='5 0 16 7 5 14 11 12 16 14'
lst=[int(i) for i in inp.split(' ')]
def zero_ind(lst):  
    for i in range(max(lst)+1):
        if i in lst:
            print(i, end=' ')
        else:
            print(0,end=' ')
zero_ind(lst)

#%%
'''
Ram shifted to a new place recently. There are multiple schools near his 
locality. Given the co-ordinates of Ram P(X,Y) and schools near his locality 
in a nested list, find the closest school. Print multiple coordinates in 
respective order if there exists multiple schools closest to him. Write a 
function closestSchool that accepts (X ,Y , L) where X and Y are co-ordinates 
of Ram's house and L contains co-ordinates of different school.

Distance Formula(To calculate distance between two co-ordinates): 
√((X2 - X1)² + (Y2 - Y1)²)

where (x1,y1) is the co-ordinate of point 1 and (x2, y2) is the 
co-ordinate of point 2.

Input:
X, Y (Ram's house co-ordinates)
N (No of schools)
X1 Y1
X2 Y2
.
.
.

X6 Y6
0 0
3
7 -6
3 -6
1 -6
Output:
Closest pont/points to X, Y
'''
data=input()
table=[]
while data:
    table.append(data.split('\n')[0])
    data=input()

ram_house=[float(i) for i in table[0].split(' ')]
n_schools=int(table[1])
lst_schools=[[float(i) for i in j.split(' ')] for j in table[2:]]

def calc_dist(X2,X1,Y2,Y1):
    return ( (X2 - X1)**2 + (Y2 - Y1)**2 )**0.5

    
def closestSchool(X,Y,L):
    closest_school_lst=[]
    
    for idx, i in enumerate(L):
        X1,Y1=i[0],i[1]
        dist=calc_dist(X, X1, Y, Y1)
        if idx==0:
            closest_dist=dist
            closest_school_lst=[i]
        else:
            if dist<closest_dist:
                closest_school_lst=[i]
                closest_dist=dist
            elif dist==closest_dist:
                closest_school_lst.append(i)
    
    return closest_school_lst


closest_school_lst= closestSchool(ram_house[0], ram_house[1], lst_schools)

for school in closest_school_lst:
    print(school)







#%%
'''
Given a string s write a program to convert uppercase letters into lowercase 
and lowercase letters into uppercase. Also print the resultant string.

Note: You need to talk the input and do not print anything while taking input.

Input:
The Joy Of Computing

Output
tHE jOY oF cOMPUTING
'''
import string

char_dict={}

for i in range(len(string.ascii_uppercase)):
    char_dict[string.ascii_uppercase[i]]=string.ascii_lowercase[i]
    char_dict[string.ascii_lowercase[i]]=string.ascii_uppercase[i]
    
def case_change(str):
    # res=''
    # for i in str:
    #     if i in char_dict.keys():
    #         res+=char_dict[i]
    #     else: res+=i
    return "fguqaBUFIAWFG DBUIqdgBUAIFGAbubuD [];',./".swapcase()

print(case_change("fguqaBUFIAWFG DBUIqdgBUAIFGAbubuD [];',./"))
    































