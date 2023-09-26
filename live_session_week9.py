# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:58:15 2023

@author: Saubhik
"""

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
list_of_fl=[(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]

def onehop(lst):
    flights={}
    for fl in lst:
        if fl[0] in flights.keys():
            flights[fl[0]].append(fl[1])
        else:flights[fl[0]]=[(fl[1])]
    # print(flights)
    
    hop=[]
    
    for dep in flights:
        arrivals=flights[dep]
        for station in arrivals:
            if station in list(flights.keys()):
                for arr in flights[station]:
                    if arr!= dep:
                        hop.append((dep,arr))
    # print(hop)
    return sorted(set(hop))

print(onehop(list_of_fl))
print(onehop([(2,3),(1,2)]))


#%%
'''
Given a Tuple T, create a function squareT that accepts one argument and 
returns a tuple containing similar elements given in tuple T and its sqaures 
in sequence.

Input:

(1,2,3)

Output :

(1,2,3,1,4,9)

Explanation:

Tuple T contains (1,2,3) the output tuple contains the original elements of 
T that is 1,2,3 and its sqaures 1,4,9 in sequence.
'''

def squareT(T):
    return T+tuple([i**2 for i in T])
print(squareT((1,2,3)))
#%%
'''
Given a string S, write a function replaceV that accepts a string and replace 
the occurrences of 3 consecutive vowels with _ in that string. Make sure to 
return and print the answer string.

Input:

aaahellooo

Output:

_hell_

Explanation:

Since aaa and ooo are consecutive 3 vowels and therefor replaced by _ .
'''
vowels=['a','e','i','o','u','A','E','I','O','U']
def replaceV(s):
    res=''
    counter=0
    for idx,char in enumerate(s):
        if char in vowels:
            counter+=1
            res+=char
            if counter==3:
                res=res.replace(s[idx-2:idx+1],'_')
                counter=0
        else:
            res+=char
            counter=0
    return res

print(replaceV('aaahellooo'))


#%%

'''
Write a program that take list L as an input and shifts all zeroes in list 
L towards the right by maintaining the order of the list. Also print the new 
list.

Input:

[0,1,0,3,12]

Output:

[1,3,12,0,0]

Explanation:

There are two zeroes in the list which are shifted to the right and the 
order of the list is also maintained. (1,3,12 are in order as in the old list.)
'''
#way 1
def zero_mover(l):
    counter=0
    while 0 in l:
        counter+=1
        l.remove(0)
    return l+[0]*counter
print(zero_mover([0,1,0,3,12]))

#way 2
def zero_mover_2(l):
    new_l=[i for i in l if i!=0]
    return new_l+[0]*(len(l)-len(new_l))
    
print(zero_mover_2([0,1,0,3,12]))






















