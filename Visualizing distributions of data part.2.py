#!/usr/bin/env python
# coding: utf-8

# In[1]:


# seaborn tutorial
# Visualizing distributions of data part.2


# In[2]:


import seaborn as sns


# ## Empirical cumulative distributions

# In[3]:


penguins = sns.load_dataset("penguins")
diamonds = sns.load_dataset("diamonds")


# In[4]:


sns.displot(penguins, x="flipper_length_mm", kind="ecdf")


# In[5]:


sns.displot(penguins, x="flipper_length_mm", hue="species", kind="ecdf")


# ## Visualizing bivariate distributions

# In[6]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm")


# In[7]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", kind="kde")


# In[8]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")


# In[9]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", kind="kde")


# In[10]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", binwidth=(2, .5))


# In[11]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", binwidth=(2, .5), cbar=True)


# In[12]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", kind="kde", thresh=.2, levels=4)


# In[13]:


sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", kind="kde", levels=[.01, .05, .1, .8])


# In[14]:


sns.displot(diamonds, x="price", y="clarity", log_scale=(True, False))


# In[15]:


sns.displot(diamonds, x="color", y="clarity")


# # Distribution visualization in other settings

# ## Plotting joint and marginal distributions

# In[16]:


sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")


# In[17]:


sns.jointplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="species",
    kind="kde"
)


# In[18]:


g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot)


# In[19]:


sns.displot(
    penguins, x="bill_length_mm", y="bill_depth_mm",
    kind="kde", rug=True
)


# In[20]:


sns.relplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
sns.rugplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")


# ## Plotting many distributions

# In[21]:


sns.pairplot(penguins)


# In[22]:


g = sns.PairGrid(penguins)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot, fill=True)
g.map_diag(sns.histplot, kde=True)

