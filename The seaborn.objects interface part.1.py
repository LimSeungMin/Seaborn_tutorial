#!/usr/bin/env python
# coding: utf-8

# In[8]:


# seaborn tutorial 
# The seaborn.objects interface part.1


# # The seaborn.objects interface

# In[9]:


import seaborn as sns


# ## Specifying a plot and mapping data

# In[10]:


import seaborn.objects as so


# In[11]:


penguins = sns.load_dataset("penguins")


# In[12]:


(
    so.Plot(penguins, x="bill_length_mm", y="bill_depth_mm")
    .add(so.Dot())
)


# ### Setting properties

# In[13]:


(
    so.Plot(penguins, x="bill_length_mm", y="bill_depth_mm")
    .add(so.Dot(color="g", pointsize=4))
)


# ### Mapping properties

# In[14]:


(
    so.Plot(
        penguins, x="bill_length_mm", y="bill_depth_mm",
        color="species", pointsize="body_mass_g",
    )
    .add(so.Dot())
)


# (
#     so.Plot(
#         penguins, x="bill_length_mm", y="bill_depth_mm",
#         edgecolor="sex", edgewidth="body_mass_g",
#     )
#     .add(so.Dot(color=".8"))
# )

# ### Defining groups

# In[16]:


healthexp = sns.load_dataset("healthexp")


# In[17]:


(
    so.Plot(healthexp, x="Year", y="Life_Expectancy", color="Country")
    .add(so.Line())
)


# In[18]:


(
    so.Plot(healthexp, x="Year", y="Life_Expectancy", group="Country")
    .add(so.Line())
)


# ## Transforming data before plotting

# ### Statistical transformation

# In[19]:


(
    so.Plot(penguins, x="species", y="body_mass_g")
    .add(so.Bar(), so.Agg())
)


# In[20]:


(
    so.Plot(penguins, x="species", y="body_mass_g")
    .add(so.Dot(pointsize=10), so.Agg())
)


# In[21]:


(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Dot(pointsize=10), so.Agg())
)


# ### Resolving overplotting

# In[22]:


(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Bar(), so.Agg())
)


# In[23]:


(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Bar(), so.Agg(), so.Dodge())
)


# In[24]:


(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Dot(), so.Dodge())
)


# In[25]:


(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Dot(), so.Dodge(), so.Jitter(.3))
)


# ### Creating variables through transformation

# In[26]:


(
    so.Plot(penguins, x="species")
    .add(so.Bar(), so.Hist())
)


# In[27]:


(
    so.Plot(penguins, x="flipper_length_mm")
    .add(so.Bars(), so.Hist())
)


# In[28]:


(
    so.Plot(penguins, x="body_mass_g", y="species", color="sex")
    .add(so.Range(), so.Est(errorbar="sd"), so.Dodge())
    .add(so.Dot(), so.Agg(), so.Dodge())
)


# ### Orienting marks and transforms

# In[29]:


(
    so.Plot(penguins, x="body_mass_g", y="species", color="sex")
    .add(so.Bar(), so.Agg(), so.Dodge())
)


# In[31]:


tips = sns.load_dataset("tips")


# In[32]:


(
    so.Plot(tips, x="total_bill", y="size", color="time")
    .add(so.Bar(), so.Agg(), so.Dodge(), orient="y")
)


# In[ ]:




