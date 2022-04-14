#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

a = np.array([[1,6], [2,8], [3,11], [3,10], [1,7]])

a


# In[4]:


mean_a = np.mean(a, axis = 0, dtype = int)

mean_a


# In[6]:


a_centered = a - mean_a

a_centered

