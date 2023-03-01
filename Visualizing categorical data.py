#!/usr/bin/env python
# coding: utf-8

# In[1]:


# seaborn tutorial
# Visualizing categorical data


# In[2]:


import seaborn as sns


# # Visualizing categorical data

# ## Categorical scatterplots

# In[3]:


tips = sns.load_dataset("tips")
sns.catplot(data=tips, x="day", y="total_bill")


# In[4]:


sns.catplot(data=tips, x="day", y="total_bill", jitter=False)


# In[5]:


sns.catplot(data=tips, x="day", y="total_bill", kind="swarm")


# In[6]:


sns.catplot(data=tips, x="day", y="total_bill", hue="sex", kind="swarm")


# In[7]:


sns.catplot(data=tips.query("size != 3"), x="size", y="total_bill")


# In[8]:


sns.catplot(data=tips, x="smoker", y="tip", order=["No", "Yes"])


# In[9]:


sns.catplot(data=tips, x="total_bill", y="day", hue="time", kind="swarm")


# ## Comparing distributions

# ### Boxplots

# In[10]:


sns.catplot(data=tips, x="day", y="total_bill", kind="box")


# In[11]:


sns.catplot(data=tips, x="day", y="total_bill", hue="smoker", kind="box")


# In[12]:


tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
sns.catplot(
    data=tips, x="day", y="total_bill", hue="weekend",
    kind="box", dodge=False,
)


# In[13]:


diamonds = sns.load_dataset("diamonds")
sns.catplot(
    data=diamonds.sort_values("color"),
    x="color", y="price", kind="boxen",
)


# ### Violinplots

# In[14]:


sns.catplot(
    data=tips, x="total_bill", y="day", hue="sex", kind="violin",
)


# In[15]:


sns.catplot(
    data=tips, x="total_bill", y="day", hue="sex",
    kind="violin", bw=.15, cut=0,
)


# In[16]:


sns.catplot(
    data=tips, x="day", y="total_bill", hue="sex",
    kind="violin", split=True,
)


# In[17]:


sns.catplot(
    data=tips, x="day", y="total_bill", hue="sex",
    kind="violin", inner="stick", split=True, palette="pastel",
)


# In[18]:


g = sns.catplot(data=tips, x="day", y="total_bill", kind="violin", inner=None)
sns.swarmplot(data=tips, x="day", y="total_bill", color="k", size=3, ax=g.ax)


# ## Estimating central tendency

# ### Bar plots

# In[19]:


titanic = sns.load_dataset("titanic")
sns.catplot(data=titanic, x="sex", y="survived", hue="class", kind="bar")


# In[20]:


sns.catplot(data=titanic, x="age", y="deck", errorbar=("pi", 95), kind="bar")


# In[21]:


sns.catplot(data=titanic, x="deck", kind="count", palette="ch:.25")


# In[22]:


sns.catplot(
    data=titanic, y="deck", hue="class", kind="count",
    palette="pastel", edgecolor=".6",
)


# ### Point plots

# In[23]:


sns.catplot(data=titanic, x="sex", y="survived", hue="class", kind="point")


# In[24]:


sns.catplot(
    data=titanic, x="class", y="survived", hue="sex",
    palette={"male": "g", "female": "m"},
    markers=["^", "o"], linestyles=["-", "--"],
    kind="point"
)


# ## Showing additional dimensions

# In[25]:


sns.catplot(
    data=tips, x="day", y="total_bill", hue="smoker",
    kind="swarm", col="time", aspect=.7,
)


# In[26]:


g = sns.catplot(
    data=titanic,
    x="fare", y="embark_town", row="class",
    kind="box", orient="h",
    sharex=False, margin_titles=True,
    height=1.5, aspect=4,
)
g.set(xlabel="Fare", ylabel="")
g.set_titles(row_template="{row_name} class")
for ax in g.axes.flat:
    ax.xaxis.set_major_formatter('${x:.0f}')

