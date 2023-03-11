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


# ## Sequential color palettes

# ### Perceptually uniform palettes

# In[3]:


sns.color_palette("rocket", as_cmap=True)


# In[4]:


sns.color_palette("mako", as_cmap=True)


# In[5]:


sns.color_palette("flare", as_cmap=True)


# In[6]:


sns.color_palette("crest", as_cmap=True)


# In[7]:


sns.color_palette("magma", as_cmap=True)


# In[8]:


sns.color_palette("viridis", as_cmap=True)


# In[9]:


sns.color_palette("rocket_r", as_cmap=True)


# ### Discrete vs. continuous mapping

# In[10]:


sns.color_palette("rocket")


# ### Sequential “cubehelix” palettes

# In[11]:


sns.color_palette("cubehelix", as_cmap=True)


# In[12]:


sns.cubehelix_palette(as_cmap=True)


# In[13]:


sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)


# In[14]:


sns.cubehelix_palette(start=.5, rot=-.75, as_cmap=True)


# In[15]:


sns.cubehelix_palette(start=2, rot=0, dark=0, light=.95, reverse=True, as_cmap=True)


# In[16]:


sns.color_palette("ch:start=.2,rot=-.3", as_cmap=True)


# In[17]:


sns.color_palette("ch:s=-.2,r=.6", as_cmap=True)


# ### Custom sequential palettes

# In[18]:


sns.light_palette("seagreen", as_cmap=True)


# In[19]:


sns.dark_palette("#69d", reverse=True, as_cmap=True)


# In[20]:


sns.color_palette("light:b", as_cmap=True)


# In[21]:


sns.color_palette("dark:salmon_r", as_cmap=True)


# ### Sequential Color Brewer palettes

# In[22]:


sns.color_palette("Blues", as_cmap=True)


# In[23]:


sns.color_palette("YlOrBr", as_cmap=True)


# ## Diverging color palettes

# ### Perceptually uniform diverging palettes

# In[24]:


sns.color_palette("vlag", as_cmap=True)


# In[25]:


sns.color_palette("icefire", as_cmap=True)


# ### Custom diverging palettes

# In[26]:


sns.diverging_palette(220, 20, as_cmap=True)


# In[27]:


sns.diverging_palette(145, 300, s=60, as_cmap=True)


# In[28]:


sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)


# ### Other diverging palettes

# In[29]:


sns.color_palette("Spectral", as_cmap=True)


# In[30]:


sns.color_palette("coolwarm", as_cmap=True)

