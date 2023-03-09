#!/usr/bin/env python
# coding: utf-8

# In[1]:


# seaborn tutorial
# Controlling figure aesthetics


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# # Controlling figure aesthetics

# In[3]:


def sinplot(n=10, flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, n + 1):
        plt.plot(x, np.sin(x + i * .5) * (n + 2 - i) * flip)


# In[4]:


sinplot()


# In[5]:


sns.set_theme()
sinplot()


# ## Seaborn figure styles

# In[6]:


sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.boxplot(data=data);


# In[7]:


sns.set_style("dark")
sinplot()


# In[8]:


sns.set_style("white")
sinplot()


# In[9]:


sns.set_style("ticks")
sinplot()


# ## Removing axes spines

# In[10]:


sinplot()
sns.despine()


# In[11]:


f, ax = plt.subplots()
sns.violinplot(data=data)
sns.despine(offset=10, trim=True);


# In[12]:


sns.set_style("whitegrid")
sns.boxplot(data=data, palette="deep")
sns.despine(left=True)


# ## Temporarily setting figure style

# In[13]:


f = plt.figure(figsize=(6, 6))
gs = f.add_gridspec(2, 2)

with sns.axes_style("darkgrid"):
    ax = f.add_subplot(gs[0, 0])
    sinplot(6)

with sns.axes_style("white"):
    ax = f.add_subplot(gs[0, 1])
    sinplot(6)

with sns.axes_style("ticks"):
    ax = f.add_subplot(gs[1, 0])
    sinplot(6)

with sns.axes_style("whitegrid"):
    ax = f.add_subplot(gs[1, 1])
    sinplot(6)

f.tight_layout()


# ## Overriding elements of the seaborn styles

# In[14]:


sns.axes_style()


# In[15]:


sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sinplot()


# ## Scaling plot elements

# In[16]:


sns.set_theme()


# In[17]:


sns.set_context("paper")
sinplot()


# In[18]:


sns.set_context("talk")
sinplot()


# In[19]:


sns.set_context("poster")
sinplot()


# In[20]:


sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sinplot()

