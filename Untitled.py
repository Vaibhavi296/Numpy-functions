#!/usr/bin/env python
# coding: utf-8

# # Creating Numpy Arrays

# In[1]:


import numpy as np


# In[2]:


arr1=np.array([1,2,3,4,5])


# In[3]:


type(arr1)


# In[4]:


arr2=np.array([[1,2,3],[4,5,6]])


# In[5]:


type(arr2)


# In[6]:


arr3=np.zeros((2,3))
arr3


# In[7]:


arr4=np.ones((3,3))
arr4


# In[8]:


arr5=np.identity(5)
arr5


# In[9]:


arr6=np.arange(5,16,2)
arr6


# In[10]:


arr7=np.linspace(10,20,5)
arr7


# In[11]:


arr8=arr7.copy()
arr8


# In[ ]:




