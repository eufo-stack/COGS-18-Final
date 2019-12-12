#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functions import *
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

#for capitalize function
assert callable(capitalize)
assert isinstance(capitalize(('hello', 'world')), np.ndarray)

#for major_type function
assert callable(major_type)
assert isinstance(major_type(('Biomed', 'Math')), np.ndarray)
assert 'STEM' in major_type(('Biomed', 'Math'))

#for support_score_table function
assert callable(support_score_table)

#for difference_of_avg function
assert callable(difference_of_avg)
table = Table().with_columns('A', range(1,5), 'B', range(1,5))
assert isinstance(difference_of_avg(table, 'A', 'B'), float)
assert difference_of_avg(table, 'A', 'B') == float(-1)

#for one_sim_stat function
assert callable(one_sim_stat)
assert isinstance(one_sim_stat(table, 'A', 'B'), float)
assert one_sim_stat(table, 'A', 'B') == float(1)

