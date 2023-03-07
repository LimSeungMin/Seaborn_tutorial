#!/usr/bin/env python
# coding: utf-8

# In[2]:


# seaborn tutorial
# Estimating regression fits


# In[3]:


import seaborn as sns
import numpy as np


# # Estimating regression fits

# ## Functions for drawing linear regression models

# In[4]:


tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips);


# In[5]:


sns.lmplot(x="total_bill", y="tip", data=tips);


# In[6]:


sns.lmplot(x="size", y="tip", data=tips);


# In[7]:


sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05);


# In[8]:


sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean);


# ## Fitting different kinds of models

# In[9]:


anscombe = sns.load_dataset("anscombe")


# In[10]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80});


# In[11]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           ci=None, scatter_kws={"s": 80});


# In[12]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80});


# In[13]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           ci=None, scatter_kws={"s": 80});


# In[14]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter_kws={"s": 80});


# In[15]:


tips["big_tip"] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x="total_bill", y="big_tip", data=tips,
           y_jitter=.03);


# In[16]:


sns.lmplot(x="total_bill", y="big_tip", data=tips,
           logistic=True, y_jitter=.03);


# In[17]:


sns.lmplot(x="total_bill", y="tip", data=tips,
           lowess=True, line_kws={"color": "C1"});


# In[18]:


sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
              scatter_kws={"s": 80});


# In[19]:


sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
              scatter_kws={"s": 80});


# ## Conditioning on other variables

# In[20]:


sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips);


# In[21]:


sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
           markers=["o", "x"], palette="Set1");


# In[22]:


sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips);


# In[23]:


sns.lmplot(x="total_bill", y="tip", hue="smoker",
           col="time", row="sex", data=tips, height=3);


# ## Plotting a regression in other contexts

# In[24]:


sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg");


# In[25]:


sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
             height=5, aspect=.8, kind="reg");


# In[26]:


sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
             hue="smoker", height=5, aspect=.8, kind="reg");

