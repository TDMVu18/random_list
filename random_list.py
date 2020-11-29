# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:33:10 2020

@author: Administrator
"""
import random
dict1={'Tên':'','Tuổi':''}
chu = ['a','b','c','d','e','f','g','h','i','j','k','l',
       'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
list1=[]
n = random.randint(50,101)
for i in range(0,n):
    dict1={'Tên':'','Tuổi':''}
    ten=''
    tuoi = random.randint(1,101)
    x = random.randint(1,10) 
    for j in range(0,x):
          t = random.randint(0,len(chu)-1)
          ten=ten+chu[t]
    dict1['Tên']=ten
    dict1['Tuổi']=tuoi
    list1.append(dict1)
print("Số phần từ của list là:",n)
print(list1)   
 

   





    
    
     