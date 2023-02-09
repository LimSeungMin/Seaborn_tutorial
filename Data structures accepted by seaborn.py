#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# seaborn tutorial 
# Data structures accepted by seaborn


# # Data structures accepted by seaborn

# In[2]:


import seaborn as sns


# ## Long-form vs. wide-form data

# ### Long-form data

# In[3]:


flights = sns.load_dataset("flights")
flights.head()


# In[4]:


sns.relplot(data=flights, x="year", y="passengers", hue="month", kind="line")


# ### Wide-form data

# In[5]:


flights_wide = flights.pivot(index="year", columns="month", values="passengers")
flights_wide.head()


# In[6]:


sns.relplot(data=flights_wide, kind="line")


# In[7]:


sns.relplot(data=flights, x="month", y="passengers", hue="year", kind="line")


# In[8]:


sns.relplot(data=flights_wide.transpose(), kind="line")


# In[9]:


sns.catplot(data=flights_wide, kind="box")


# ![image.png](attachment:image.png)

# ### Messy data

# In[10]:


anagrams = sns.load_dataset("anagrams")
anagrams


# In[11]:


anagrams_long = anagrams.melt(id_vars=["subidr", "attnr"], var_name="solutions", value_name="score")
anagrams_long.head()


# In[12]:


sns.catplot(data=anagrams_long, x="solutions", y="score", hue="attnr", kind="point")


# ## Options for visualizing long-form data

# In[13]:


flights_dict = flights.to_dict()
sns.relplot(data=flights_dict, x="year", y="passengers", hue="month", kind="line")


# In[14]:


flights_avg = flights.groupby("year").mean()
sns.relplot(data=flights_avg, x="year", y="passengers", kind="line")


# In[15]:


var(/folders/qk/cdrdfhfn5g554pnb30pp4ylr0000gn/T/ipykernel_77263/885836857.py:1:, FutureWarning:, The, default, value, of, numeric_only, in, DataFrameGroupBy.mean, is, deprecated., In, a, future, version,, numeric_only, will, default, to, False., Either, specify, numeric_only, or, select, only, columns, which, should, be, valid, for, the, function.)
  flights_avg = flights.groupby("year").mean()


# In[16]:


year = flights_avg.index
passengers = flights_avg["passengers"]
sns.relplot(x=year, y=passengers, kind="line")


# In[17]:


sns.relplot(x=year.to_numpy(), y=passengers.to_list(), kind="line")


# ## Options for visualizing wide-form data

# In[18]:


flights_wide_list = [col for _, col in flights_wide.items()]
sns.relplot(data=flights_wide_list, kind="line")


# In[19]:


two_series = [flights_wide.loc[:1955, "Jan"], flights_wide.loc[1952:, "Aug"]]
sns.relplot(data=two_series, kind="line")


# In[20]:


two_arrays = [s.to_numpy() for s in two_series]
sns.relplot(data=two_arrays, kind="line")


# In[21]:


two_arrays_dict = {s.name: s.to_numpy() for s in two_series}
sns.relplot(data=two_arrays_dict, kind="line")


# In[22]:


flights_array = flights_wide.to_numpy()
sns.relplot(data=flights_array, kind="line")

