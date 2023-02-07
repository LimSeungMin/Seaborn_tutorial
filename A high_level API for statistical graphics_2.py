#!/usr/bin/env python
# coding: utf-8

# In[4]:


# seaborn tutorial 
# An introduction to seaborn
# part 2


# In[5]:


# import seaborn
import seaborn as sns


# In[6]:


# Multivariate views on complex datasets
# 복잡한 데이터 세트에 대한 다변량 보기


# In[7]:


# jointplot 단일 관계에 중점. 각 변수의 주변 분포와 함께 두 변수 간의 결합 분포를 플로팅.
penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")


# In[8]:


# pairplot 모든 쌍별 관계와 각 변수에 대한 공동 및 한계 분포를 각각 보여줌
sns.pairplot(data=penguins, hue="species")


# In[9]:


# Lower-level tools for building figures
# 수치 작성을 위한 하위 수준 도구


# In[10]:


g = sns.PairGrid(penguins, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))


# In[11]:


# Opinionated defaults and flexible customization
# 신중한 기본값 및 유연한 사용자 정의


# In[12]:


sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g"
)


# In[13]:


sns.set_theme(style="ticks", font_scale=1.25)
g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
    palette="crest", marker="x", s=100,
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
g.legend.set_title("Body mass (g)")
g.figure.set_size_inches(6.5, 4.5)
g.ax.margins(.15)
g.despine(trim=True)


# In[ ]:




