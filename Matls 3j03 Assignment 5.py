#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from statsmodels.formula.api import ols
import numpy as np
import matplotlib.pyplot as plt

BacterialGrowth = pd.read_csv(r'C:\Users\20170\Downloads\Assignment5_v01\Assignment5_v01\BacterialGrowth.csv',delimiter=';');
BacterialGrowth

y_transformed = np.log(BacterialGrowth['PopulationSize'])
y_transformed

model = ols("PopulationSize~Time_hours", {'Time_hours': BacterialGrowth['Time_hours'], 'PopulationSize': y_transformed})
results = model.fit()
print(results.summary())


# In[5]:


import matplotlib.pyplot as plt
import numpy as np


y_pred = 1.6921 + 1.0654*BacterialGrowth['Time_hours']
y_original = np.exp(y_pred)
error = BacterialGrowth['PopulationSize'] - y_original
plt.scatter(BacterialGrowth['Time_hours'], error)


# In[ ]:




