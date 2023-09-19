# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:15:40 2023

@author: saubh
"""
#%%
my_dict={'match1':{'player1':57, 'player2':38}, 
         'match2':{'player3':9, 'player1':42}, 
         'match3':{'player2':41, 'player4':63, 'player3':91}}

def orangecap(d):
    player_scores={}
    
    for match in d: #iterating each match
        scorecard=d[match]
        for player in scorecard: #iterating for each player
            curr_score=scorecard[player]
            try:
                player_scores[player]+=curr_score
            except KeyError:
                player_scores[player]=curr_score
    
    max_scorer=['',0]
    for player in player_scores:
        if max_scorer[1]<player_scores[player]:
            max_scorer=[player,player_scores[player]]
    print(max_scorer)
    

orangecap(my_dict)
#%%
with open('univ_scores.txt','r') as f:
    data=f.readlines()

grade_dict={'A':10, 'AB':9, 'B':8, 'BC':7, 'C':6, 'CD':5, 'D':4}

course_idx, student_idx, grade_idx=0,0,0

#getting indices for getting scores
for i in range(len(data)):
    if data[i]=='Courses\n':
        course_idx=i
    elif data[i]=='Students\n':
        student_idx=i
    elif data[i]=='Grades\n':
        grade_idx=i

#lists of diiferent items
courses=data[course_idx+1:student_idx]
students=data[student_idx+1:grade_idx]
grades=data[grade_idx+1:len(data)-1]

#making the base student dictionary in the following format:
    #student_dict={roll==>[name,{courses==>course:grades(initiated with 0)}]}
student_dict={}
for i in students:
    roll=i.split('~')[0]
    name=i.split('~')[1].strip('\n')
    student_dict[roll]=[name,{}]
    for k in courses:
        course=k.split('~')[0]
        student_dict[roll][1][course]=0
    
#updating the grades for each course for each student 
for j in grades:
    j.split('~')
    roll=j.split('~')[3]
    course=j.split('~')[0]
    grade=grade_dict[j.split('~')[-1].strip('\n')]
    student_dict[roll][1][course]=grade

#calculating GPAs and printing in required format
for key in sorted(student_dict):
    grade_point_avg=round(sum(student_dict[key][1].values())/len(student_dict[key][1].values()),2)
    print(key,student_dict[key][0],grade_point_avg,sep='~')


















