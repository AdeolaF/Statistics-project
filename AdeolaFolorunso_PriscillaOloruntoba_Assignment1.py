#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
film_thickness = pd.read_excel(r'C:\Users\20170\Desktop\MATLS3J03_Assignment1_v03\MATLS3J03_Assignment1_v03\Data sets\A1_FilmThickness.xlsx');


import matplotlib.pyplot as plt

first_hundred_rows = film_thickness.iloc[1:100]
color = {
    "boxes": "Black",
    "whiskers": "Black",
    "medians": "Black",
    "caps": "Black",
}
axis = first_hundred_rows.plot.box(color=color, sym="r+",figsize=(10,6),fontsize=14,grid=False);
axis.set_xlabel("Position", {'size': 16})
axis.set_ylabel("Film thickness(µm)", {'size': 16})
plt.title('Film thickness vs Position',{'size': 16})
plt.show()


Energy_Consumption = pd.read_excel(r'C:\Users\20170\Desktop\MATLS3J03_Assignment1_v03\MATLS3J03_Assignment1_v03\Data sets\A1_EnergyConsumption_v2.xlsx',parse_dates=["MonthDay"],usecols="A,C")
first_fifty_rows = Energy_Consumption.iloc[0:140]
first_fifty_rows.plot(x='MonthDay', y='Consumption')
plt.ylabel('Energy Consumption(kWh)', {'size': 12})
plt.title('Energy Consumption over time')
plt.show()

Energy_Consumption = pd.read_excel(r'C:\Users\20170\Desktop\MATLS3J03_Assignment1_v03\MATLS3J03_Assignment1_v03\Data sets\A1_EnergyConsumption_v2.xlsx',parse_dates=["Hour of day"],usecols="B,C")
first_fifty_rows = Energy_Consumption.iloc[0:500]
first_fifty_rows.plot(x='Hour of day', y='Consumption')
plt.ylabel('Energy Consumption(kWh)', {'size': 12})
plt.title('Energy Consumption vs Time of Day')
plt.show()

Energy_Consumption = pd.read_excel(r'C:\Users\20170\Desktop\MATLS3J03_Assignment1_v03\MATLS3J03_Assignment1_v03\Data sets\A1_EnergyConsumption_v2.xlsx',parse_dates=["Hour of day"],usecols="B,C")
first_fifty_rows = Energy_Consumption.iloc[0:2711]
first_fifty_rows.plot.scatter(x='Hour of day', y='Consumption')
plt.ylabel('Energy Consumption(kWh)', {'size': 12})
plt.title('Energy Consumption vs Time of Day')
plt.show()




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




