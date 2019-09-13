
# coding: utf-8

# In[1]:


import pandas as pd 

read = pd.read_csv('2018-2010_export.csv')
r = read.corr()
r

