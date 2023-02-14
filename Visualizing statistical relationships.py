#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# seaborn tutorial
# Visualizing statistical relationships


# # Visualizing statistical relationships

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")


# ## Relating variables with scatter plots

# In[3]:


tips = sns.load_dataset("tips")
sns.relplot(data=tips, x="total_bill", y="tip")


# In[4]:


sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker")


# In[5]:


sns.relplot(
    data=tips,
    x="total_bill", y="tip", hue="smoker", style="smoker"
)


# In[6]:


sns.relplot(
    data=tips,
    x="total_bill", y="tip", hue="smoker", style="time",
)


# In[7]:


sns.relplot(
    data=tips, x="total_bill", y="tip", hue="size",
)


# In[8]:


sns.relplot(
    data=tips,
    x="total_bill", y="tip",
    hue="size", palette="ch:r=-.5,l=.75"
)


# In[9]:


sns.relplot(data=tips, x="total_bill", y="tip", size="size")


# In[11]:


sns.relplot(
    data=tips, x="total_bill", y="tip",
    size="size", sizes=(15, 200)
)


# ## Emphasizing continuity with line plots

# In[12]:


dowjones = sns.load_dataset("dowjones")
sns.relplot(data=dowjones, x="Date", y="Price", kind="line")


# ### Aggregation and representing uncertainty

# In[13]:


fmri = sns.load_dataset("fmri")
sns.relplot(data=fmri, x="timepoint", y="signal", kind="line")


# In[14]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", errorbar=None,
)


# In[15]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", errorbar="sd",
)


# In[16]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal",
    estimator=None,
)


# ### Plotting subsets of data with semantic mappings

# In[17]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", hue="event",
)


# In[18]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal",
    hue="region", style="event",
)


# In[19]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", hue="region", style="event",
    dashes=False, markers=True,
)


# In[20]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", hue="event", style="event",
)


# In[21]:


sns.relplot(
    data=fmri.query("event == 'stim'"), kind="line",
    x="timepoint", y="signal", hue="region",
    units="subject", estimator=None,
)


# In[22]:


dots = sns.load_dataset("dots").query("align == 'dots'")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate",
    hue="coherence", style="choice",
)


# In[23]:


palette = sns.cubehelix_palette(light=.8, n_colors=6)
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate",
    hue="coherence", style="choice", palette=palette,
)


# In[24]:


from matplotlib.colors import LogNorm
palette = sns.cubehelix_palette(light=.7, n_colors=6)
sns.relplot(
    data=dots.query("coherence > 0"), kind="line",
    x="time", y="firing_rate",
    hue="coherence", style="choice",
    hue_norm=LogNorm(),
)


# In[25]:


sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate",
    size="coherence", style="choice",
)


# In[26]:


sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate",
    hue="coherence", size="choice", palette=palette,
)


# ### Controlling sorting and orientation

# In[27]:


healthexp = sns.load_dataset("healthexp").sort_values("Year")
sns.relplot(
    data=healthexp, kind="line",
    x="Spending_USD", y="Life_Expectancy", hue="Country",
    sort=False
)


# In[28]:


sns.relplot(
    data=fmri, kind="line",
     x="signal", y="timepoint", hue="event",
    orient="y",
)


# ## Showing multiple relationships with facets

# In[29]:


sns.relplot(
    data=tips,
    x="total_bill", y="tip", hue="smoker", col="time",
)


# In[30]:


sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", hue="subject",
    col="region", row="event", height=3,
    estimator=None
)


# In[31]:


sns.relplot(
    data=fmri.query("region == 'frontal'"), kind="line",
    x="timepoint", y="signal", hue="event", style="event",
    col="subject", col_wrap=5,
    height=3, aspect=.75, linewidth=2.5,
)

