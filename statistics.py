import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

#Employee salaries (in thousand Rs.)
salary = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#Central Tendency - where is the center of data ?
mean = np.mean(salary)
median = np.median(salary)
mode = stats.mode(salary, keepdims = True).mode[0]

print(f'Mean (Average) : Rs.{mean:.1f}K')
print(f'Median (Middle value) : Rs.{median:.1f}K')
print(f'Mode (Most common) : Rs.{mode}K')

#Spread - how varied is the data ?
std = np.std(salary)    #Standard Variation
var = np.var(salary)    #Variance (std squared)
rng = max(salary) - min(salary)  #Range
q1 = np.percentile(salary, 25)   #25th Percentile
q3 = np.percentile(salary, 75)   #75th Percentile
iqr = q3 - q1                    #Interquartile Range

print(f'Standard Deviation : Rs.{std:.2f}K (most important spread measure)')
print(f'IQR : {iqr}K (Q1 = {q1}, Q3 = {q3})')

#Outlier detection using IQR (Interquartile Range)
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = [x for x in salary if x < lower or x > upper]
print(f'Outliers : {outliers}')