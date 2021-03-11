#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


from pathlib import Path


# In[4]:


csvpath = Path('pybank.csv')


# In[5]:


df = pd.read_csv(csvpath)


# In[6]:


total_months = df.shape[0]


# In[7]:


df.head(10)


# In[8]:


total_profits_losses = df['Profit/Losses'].sum()


# In[9]:


df['P/L Shifted'] = df['Profit/Losses'].shift(1)
df['Difference of P/L and Shifted'] = df['Profit/Losses'] - df['P/L Shifted']
df.head(10)


# In[12]:


average = df['Difference of P/L and Shifted'].mean()
maximum_increase_profits = df['Difference of P/L and Shifted'].max()
maximum_increase_losses = df['Difference of P/L and Shifted'].min()
#print(f'average|{average}')
#print(f'max|{maximum_increase_profits}')
#print(f'min|{maximum_increase_losses}')


# In[13]:


print('Financial Analysis')
print('-' * 25)
print(f'Total Months: {total_months}')
print(f'Total Profits/Losses: ${total_profits_losses}')
print(f'Average Change: ${average}')
print(f'Greatest Increase In Profits: ${maximum_increase_profits}')
print(f'Greates Decrease In Profits: ${maximum_increase_losses}')


# In[ ]:





# In[ ]:




