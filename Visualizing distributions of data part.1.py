#!/usr/bin/env python
# coding: utf-8

# In[3]:


# seaborn tutorial
# Visualizing distributions of data part.1


# In[4]:


import seaborn as sns


# # Visualizing distributions of data

# ## Plotting univariate histograms

# In[5]:


penguins = sns.load_dataset("penguins")
sns.displot(penguins, x="flipper_length_mm")


# ### Choosing the bin size

# In[6]:


sns.displot(penguins, x="flipper_length_mm", binwidth=3)


# In[7]:


sns.displot(penguins, x="flipper_length_mm", bins=20)


# In[8]:


tips = sns.load_dataset("tips")
sns.displot(tips, x="size")


# In[9]:


sns.displot(tips, x="size", bins=[1, 2, 3, 4, 5, 6, 7])


# In[10]:


sns.displot(tips, x="size", discrete=True)


# In[11]:


sns.displot(tips, x="day", shrink=.8)


# ### Conditioning on other variables

# In[12]:


sns.displot(penguins, x="flipper_length_mm", hue="species")


# In[13]:


sns.displot(penguins, x="flipper_length_mm", hue="species", element="step")


# In[14]:


sns.displot(penguins, x="flipper_length_mm", hue="species", multiple="stack")


# In[15]:


sns.displot(penguins, x="flipper_length_mm", hue="sex", multiple="dodge")


# In[16]:


sns.displot(penguins, x="flipper_length_mm", col="sex")


# ### Normalized histogram statistics

# In[17]:


sns.displot(penguins, x="flipper_length_mm", hue="species", stat="density")


# In[18]:


sns.displot(penguins, x="flipper_length_mm", hue="species", stat="density", common_norm=False)


# In[19]:


sns.displot(penguins, x="flipper_length_mm", hue="species", stat="probability")


# ## Kernel density estimation

# In[20]:


sns.displot(penguins, x="flipper_length_mm", kind="kde")


# ### Choosing the smoothing bandwidth

# In[21]:


sns.displot(penguins, x="flipper_length_mm", kind="kde", bw_adjust=.25)


# In[22]:


sns.displot(penguins, x="flipper_length_mm", kind="kde", bw_adjust=2)


# ### Conditioning on other variables

# In[23]:


sns.displot(penguins, x="flipper_length_mm", hue="species", kind="kde")


# In[24]:


sns.displot(penguins, x="flipper_length_mm", hue="species", kind="kde", multiple="stack")


# In[25]:


sns.displot(penguins, x="flipper_length_mm", hue="species", kind="kde", fill=True)


# ### Kernel density estimation pitfalls

# In[26]:


sns.displot(tips, x="total_bill", kind="kde")


# In[27]:


sns.displot(tips, x="total_bill", kind="kde", cut=0)


# In[28]:


diamonds = sns.load_dataset("diamonds")
sns.displot(diamonds, x="carat", kind="kde")


# In[29]:


sns.displot(diamonds, x="carat")


# In[30]:


sns.displot(diamonds, x="carat", kde=True)

