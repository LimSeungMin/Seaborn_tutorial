#!/usr/bin/env python
# coding: utf-8

# In[2]:


# seaborn tutorial 
# An introduction to seaborn
# part 1


# In[3]:


# import seaborn
import seaborn as sns

# apply the default theme
sns.set_theme()

# load an example dataset
tips = sns.load_dataset("tips")

# create a visualiztion
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size"
)


# In[9]:


dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
    )


# In[10]:


# Statistical estimation
# 통계적 추정
fmri = sns.load_dataset("fmri")
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)


# In[11]:


sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")


# In[13]:


# Distributional representations
# 분포 표현
sns.displot(data=tips, x="total_bill", col="time", kde=True)


# In[14]:


sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)


# In[15]:


# Plots for categorical data
# 범주형 데이터에 대한 플롯
sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")


# In[16]:


sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)


# In[17]:


sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")

