#!/usr/bin/env python
# coding: utf-8

# In[1]:


# seaborn tutorial
# Choosing color palettes


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# # Choosing color palettes

# ## Qualitative color palettes

# In[3]:


sns.color_palette()


# In[4]:


sns.color_palette("tab10")


# ### Using circular color systems

# In[5]:


sns.color_palette("hls", 8)


# In[6]:


sns.color_palette("husl", 8)


# ### Using categorical Color Brewer palettes

# In[7]:


sns.color_palette("Set2")


# In[8]:


sns.color_palette("Paired")

