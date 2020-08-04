#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


ser = pd.Series(np.random.random(5), name = 'Column 01')


# In[4]:


ser


# In[5]:


from pandas_datareader import data as wb


# In[6]:


PG = wb.DataReader('PG', data_source = 'yahoo', start = '1995-1-1')


# In[7]:


PG


# In[10]:


Apple = wb.DataReader('AAPL', data_source = 'yahoo', start = '2020-1-1')


# In[11]:


Apple


# In[16]:


Microsoft = wb.DataReader('MSFT', data_source = 'yahoo', start = '2020-1-1')


# In[17]:


Microsoft


# In[ ]:




