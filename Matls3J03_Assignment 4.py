#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd

ReactorData = pd.read_csv(r'C:\Users\20170\Downloads\Assignment 4\Assignment 4\ReactorData.csv',delimiter=';');
ReactorData


# In[25]:


import matplotlib.pyplot as plt
ReactorData.plot.scatter(x="Temp_C",y="Yield_g")
plt.title('Yield vs Temperature')


# In[14]:


from statsmodels.formula.api import ols

model = ols("Yield_g ~ Temp_C", ReactorData)
results = model.fit()
print(results.summary())
import math
standard_error = results.scale
standard_error=math.sqrt(standard_error)
print("The model standard error is: " + str(standard_error))


# In[ ]:





# In[16]:


import math
import pandas as pd
ReactorData = pd.read_csv(r'C:\Users\20170\Downloads\Assignment 4\Assignment 4\ReactorData.csv',delimiter=';');
from statsmodels.formula.api import ols
model = ols("Yield_g ~ Temp_C+Speed_100RPM+Baffles", ReactorData)
results = model.fit()
print(results.summary())
import math
standard_error = results.scale
standard_error=math.sqrt(standard_error)
print("The model standard error is: " + str(standard_error))


# In[17]:


import math
import pandas as pd
ReactorData = pd.read_csv(r'C:\Users\20170\Downloads\Assignment 4\Assignment 4\ReactorData.csv',delimiter=';');
from statsmodels.formula.api import ols
model = ols("Yield_g ~ Temp_C+Speed_100RPM", ReactorData)
results = model.fit()
print(results.summary())
import math
standard_error = results.scale
standard_error=math.sqrt(standard_error)
print("The model standard error is: " + str(standard_error))


# In[ ]:




