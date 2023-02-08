#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# seaborn tutorial 
# Overview of seaborn plotting functions


# In[8]:


# import seaborn
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Similar functions for similar tasks
penguins = sns.load_dataset("penguins")

# histplot
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")


# In[3]:


# kdeplot
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")


# ## Figure-level vs. axes-level functions

# ![image.png](attachment:image.png)

# In[4]:


# displot
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")


# In[5]:


# displot(kind="kde")
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", kind="kde")


# In[6]:


# displot
sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="species")


# ### Axes-level functions make self-contained plots

# In[9]:


f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0])
sns.histplot(data=penguins, x="species", hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[1])
f.tight_layout()


# ### Figure-level functions own their figure

# In[10]:


tips = sns.load_dataset("tips")
g = sns.relplot(data=tips, x="total_bill", y="tip")
g.ax.axline(xy1=(10, 2), slope=.2, color="b", dashes=(5, 2))


# ### Customizing plots from a figure-level function

# In[11]:


g = sns.relplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", col="sex")
g.set_axis_labels("Flipper length (mm)", "Bill length (mm)")


# ### Specifying figure sizes

# In[12]:


f, ax = plt.subplots()


# In[13]:


f, ax = plt.subplots(1, 2, sharey=True)


# In[14]:


g = sns.FacetGrid(penguins)


# In[15]:


g = sns.FacetGrid(penguins, col="sex")


# In[16]:


g = sns.FacetGrid(penguins, col="sex", height=3.5, aspect=.75)


# ### Relative merits of figure-level functions

# ![image.png](attachment:image.png)

# # Combining multiple views on the data

# In[17]:


# jointplot
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")


# In[18]:


# pairplot
sns.pairplot(data=penguins, hue="species")


# In[19]:


# jointplot(kind="hist")
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", kind="hist")

