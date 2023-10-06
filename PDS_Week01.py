# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:47:28 2023

@author: saund
"""
#DIY PART-1

import csv

i = 0
val = 0
    
f = open("TB_burden_countries_2014-09-29.csv")
next(f)

for row in csv.reader(f):
    try:
        new_val = float(row[11])  

    except:
        new_val = 0   
    val = val + float(new_val)
            
    i+=1

print('row count: ', i)
print('average value of e_prev_num_lo: ',val/i)


# 1990
i = 0
val = 0
f = open("TB_burden_countries_2014-09-29.csv")
next(f)

for row in csv.reader(f):
    if row[5] == '1990':
        try:
            new_val = float(row[11])  

        except:
            new_val = 0   
        val = val + float(new_val)
                
        i+=1

print('row count in 1990: ', i)
print('average value of e_prev_num_lo in 2011: ',val/i)

#2011
i = 0
val = 0
f = open("TB_burden_countries_2014-09-29.csv")
next(f)

for row in csv.reader(f):
    if row[5] == '2011':
        try:
            new_val = float(row[11])  

        except:
            new_val = 0   
        val = val + float(new_val)
                
        i+=1

print('row count in 2011: ', i)
print('average value of e_prev_num_lo in 2011: ',val/i)

#DIY PART - 2

import numpy as np
import matplotlib.pyplot as plt

q1 = np.arange(5, 16)
q2 = np.linspace(0, 23, 7)

uniform_array = np.random.uniform(-1, 1, size=10)
plt.hist(uniform_array)
plt.show()

a1 = np.random.rand(10)
a2 = np.random.rand(10)
distance = np.sqrt(np.sum((a1 - a2)**2))
print("distance: ", distance)