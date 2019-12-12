#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from datascience import *
import random
import math
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)

#capitalizes the first letter of each word in array
def capitalize(array):
    capped_string = []
    for i in array:
        x = np.char.title(i)
        capped_string = np.append(capped_string, x)
    return capped_string

#categorize majors into STEM and Non STEM
def major_type(array):
    typed = ()
    for i in array:
        if 'Engineer' in i:
            a = 'STEM'
            typed = np.append(typed, a)
        elif 'Bio' in i:
            a = 'STEM'
            typed = np.append(typed, a)
        elif 'Math' in i:
            a = 'STEM'
            typed = np.append(typed, a)
        elif 'Chem' in i:
            a = 'STEM'
            typed = np.append(typed, a)
        elif 'Comp' in i:
            a = 'STEM'
            typed = np.append(typed, a)
        elif 'Cog' in i:
            a = 'STEM'
            typed = np.append(typed, a)
        elif 'Data' in i:
            a = 'STEM'
            typed = np.append(typed, a)
        else:
            a = 'Non STEM'
            typed = np.append(typed, a)
    return typed

#creates the Support Score and new table
def support_score_table(table, col_a, col_b):
    support_score = table.column(col_a) + table.column(col_b)
    new_table = table.with_column('Support Score', support_score).select(0,1,4)
    return new_table

#calculates observed test statistic
def difference_of_avg(table, label, group_label):
    relevant_columns = table.select(label, group_label)
    mean_table = relevant_columns.group(group_label, np.average)
    mean = mean_table.column(1)
    return mean.item(0) - mean.item(1)

#randomizes major type and calculates 1 simulated test statistic
def one_sim_stat(table, label, group_label):
    random_type = table.sample(with_replacement = False
                                                    ).column(group_label)
    random_table = table.select(label).with_column(
        'Random Major Type', random_type)
    return difference_of_avg(random_table, label, 'Random Major Type')




