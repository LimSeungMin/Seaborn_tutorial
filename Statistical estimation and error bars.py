#!/usr/bin/env python
# coding: utf-8

# In[1]:


# seaborn tutorial
# Statistical estimation and error bars


# In[2]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# # Statistical estimation and error bars

# In[3]:


def plot_errorbars(arg, **kws):
    np.random.seed(sum(map(ord, "error_bars")))
    x = np.random.normal(0, 1, 100)
    f, axs = plt.subplots(2, figsize=(7, 2), sharex=True, layout="tight")
    sns.pointplot(x=x, errorbar=arg, **kws, capsize=.3, ax=axs[0])
    sns.stripplot(x=x, jitter=.3, ax=axs[1])


# ## Measures of data spread

# ### Standard deviation error bars

# In[4]:


plot_errorbars("sd")


# ### Percentile interval error bars

# In[5]:


plot_errorbars(("pi", 50))


# ## Measures of estimate uncertainty

# ### Standard error bars

# In[6]:


plot_errorbars("se")


# ### Confidence interval error bars

# In[7]:


plot_errorbars("ci")


# In[8]:


plot_errorbars(("se", 2))


# In[9]:


plot_errorbars("ci", estimator="median")


# In[10]:


plot_errorbars("ci", n_boot=5000, seed=10)


# ### Custom error bars

# In[11]:


plot_errorbars(lambda x: (x.min(), x.max()))


# ## Error bars on regression fits

# In[12]:


x = np.random.normal(0, 1, 50)
y = x * 2 + np.random.normal(0, 2, size=x.size)
sns.regplot(x=x, y=y)

