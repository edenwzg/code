# In[1]:

import pandas as pd
import numpy as numpy

df = pd.read_excel('d:/code/excel-comp-data.xlsx')
df.head()

# In[]
df['total'] = df['Jan'] + df['Feb'] + df['Mar']
df.head()

# In[2]:

print df['Jan'].sum(), df['Jan'].mean(), df['Jan'].min(), df['Jan'].max()
obj = df[['Jan', 'Feb', 'Mar', 'total']]
print obj


# In[3]:
sum_row = df[['Jan', 'Feb', 'Mar', 'total']].sum()
print sum_row

# In[]
