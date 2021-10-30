#!/usr/bin/env python
# coding: utf-8

# In[25]:


import statsmodels.graphics.gofplots as sm
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import math
import scipy.stats as stats

Seedling_Height = pd.read_excel(r'C:\Users\20170\Downloads\MATLS3J03_Assignment2_v01\A2_SeedlingHeight.xlsx')
Seedling_Height.describe()


# In[22]:


Seedling_Height.hist(color='k',bins=8,grid=False)


# In[26]:


stats.probplot(Seedling_Height['Seedling Height'], dist="norm", plot=plt);
plt.show()


# In[34]:


Sorted_data=Seedling_Height.sort_values("Seedling Height");
mean=Seedling_Height.mean()
std=Seedling_Height.std()
z=(18-mean)/std
p_z = 1 - norm.cdf(z)
print("p_z is",p_z)


# In[ ]:




