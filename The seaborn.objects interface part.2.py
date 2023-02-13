#!/usr/bin/env python
# coding: utf-8

# In[1]:


# seaborn tutorial 
# The seaborn.objects interface part.2


# ## Building and displaying the plot

# ### Adding multiple layers

# In[2]:


import seaborn as sns
import seaborn.objects as so
import matplotlib as mpl


# In[3]:


tips = sns.load_dataset("tips")


# In[4]:


(
    so.Plot(tips, x="total_bill", y="tip")
    .add(so.Dots())
    .add(so.Line(), so.PolyFit())
)


# In[5]:


(
    so.Plot(tips, x="total_bill", y="tip", color="time")
    .add(so.Dots())
    .add(so.Line(), so.PolyFit())
)


# ### Layer-specific mappings

# In[6]:


(
    so.Plot(tips, x="total_bill", y="tip")
    .add(so.Dots(), color="time")
    .add(so.Line(color=".2"), so.PolyFit())
)


# In[7]:


(
    so.Plot(tips, x="total_bill", y="tip", color="time")
    .add(so.Dots())
    .add(so.Line(color=".2"), so.PolyFit(), color=None)
)


# ![image.png](attachment:image.png)

# ### Faceting and pairing subplots

# In[8]:


penguins = sns.load_dataset("penguins")
healthexp = sns.load_dataset("healthexp")
diamonds = sns.load_dataset("diamonds")


# In[9]:


(
    so.Plot(penguins, x="flipper_length_mm")
    .facet("species")
    .add(so.Bars(), so.Hist())
)


# In[10]:


(
    so.Plot(penguins, x="flipper_length_mm")
    .facet(col="species", row="sex")
    .add(so.Bars(), so.Hist())
)


# In[11]:


(
    so.Plot(healthexp, x="Year", y="Life_Expectancy")
    .facet(col="Country", wrap=3)
    .add(so.Line())
)


# In[12]:


(
    so.Plot(healthexp, x="Year", y="Life_Expectancy")
    .facet("Country", wrap=3)
    .add(so.Line(alpha=.3), group="Country", col=None)
    .add(so.Line(linewidth=3))
)


# In[13]:


(
    so.Plot(penguins, y="body_mass_g", color="species")
    .pair(x=["bill_length_mm", "bill_depth_mm"])
    .add(so.Dots())
)


# In[14]:


(
    so.Plot(penguins, y="body_mass_g", color="species")
    .pair(x=["bill_length_mm", "bill_depth_mm"])
    .facet(row="sex")
    .add(so.Dots())
)


# ### Integrating with matplotlib

# In[15]:


f = mpl.figure.Figure(figsize=(8, 4))
sf1, sf2 = f.subfigures(1, 2)
(
    so.Plot(penguins, x="body_mass_g", y="flipper_length_mm")
    .add(so.Dots())
    .on(sf1)
    .plot()
)
(
    so.Plot(penguins, x="body_mass_g")
    .facet(row="sex")
    .add(so.Bars(), so.Hist())
    .on(sf2)
    .plot()
)


# ### Building and displaying the plot

# In[16]:


p = so.Plot(healthexp, "Year", "Spending_USD", color="Country")


# In[17]:


p.add(so.Line())


# In[18]:


p.add(so.Area(), so.Stack())


# ## Customizing the appearance

# ### Parameterizing scales

# In[19]:


(
    so.Plot(diamonds, x="carat", y="price")
    .add(so.Dots())
    .scale(y="log")
)


# In[20]:


(
    so.Plot(diamonds, x="carat", y="price", color="clarity")
    .add(so.Dots())
    .scale(color="flare")
)


# In[21]:


(
    so.Plot(diamonds, x="carat", y="price", color="clarity", pointsize="carat")
    .add(so.Dots())
    .scale(color=("#88c", "#555"), pointsize=(2, 10))
)


# In[22]:


(
    so.Plot(diamonds, x="carat", y="price", color="carat", marker="cut")
    .add(so.Dots())
    .scale(
        color=so.Continuous("crest", norm=(0, 3), trans="sqrt"),
        marker=so.Nominal(["o", "+", "x"], order=["Ideal", "Premium", "Good"]),
    )
)


# In[23]:


# /Users/mwaskom/code/seaborn/seaborn/_core/properties.py:370: RuntimeWarning: invalid value encountered in cast
#   ixs = np.asarray(x, np.intp)


# ### Customizing legends and ticks

# In[24]:


(
    so.Plot(diamonds, x="carat", y="price", color="carat")
    .add(so.Dots())
    .scale(
        x=so.Continuous().tick(every=0.5),
        y=so.Continuous().label(like="${x:.0f}"),
        color=so.Continuous().tick(at=[1, 2, 3, 4]),
    )
)


# ### Customizing limits, labels, and titles

# In[25]:


(
    so.Plot(penguins, x="body_mass_g", y="species", color="island")
    .facet(col="sex")
    .add(so.Dot(), so.Jitter(.5))
    .share(x=False)
    .limit(y=(2.5, -.5))
    .label(
        x="Body mass (g)", y="",
        color=str.capitalize,
        title="{} penguins".format,
    )
)


# ### Theme customization

# In[26]:


from seaborn import axes_style
so.Plot().theme({**axes_style("whitegrid"), "grid.linestyle": ":"})


# In[ ]:




