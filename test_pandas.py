
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


s = pd.Series([1,3,5,np.nan,6,8])
s


# In[3]:


s.index


# In[4]:


dates = pd.date_range('2013-01-01', periods=6)
dates


# In[7]:


df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df


# In[11]:


df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D':np.array([3] * 4, dtype='int32'),
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'foo'
                   })
df2


# In[12]:


df2.dtypes


# In[13]:


df = get_price('000001.XSHE','2017-06-01','2017-06-14','1d',['open','high','low','close'])
df


# In[14]:


df.head()


# In[15]:


df.tail()


# In[16]:


df.index


# In[17]:


df.columns


# In[18]:


df.values


# In[19]:


df.describe()


# In[20]:


df.T


# In[21]:


df.sort_index(axis=1, ascending=False)


# In[23]:


df.sort_values(by='open', ascending=False)


# In[24]:


df['open']


# In[25]:


df[['open','close']]


# In[26]:


df[0:3]


# In[27]:


df['2017-06-01':'2017-06-05']


# In[28]:


df.loc['2017-06-01','open']


# In[29]:


df.loc['2017-06-01':'2017-06-06']


# In[30]:


df.loc[:,'open']


# In[33]:


df.loc['2017-06-01':'2017-6-06','open']


# In[34]:


df.iloc[1,1]


# In[35]:


df.iloc[[0,2],:]


# In[36]:


df.iloc[0:2,:]


# In[37]:


df.iloc[:,1]


# In[38]:


df.iloc[1,:]


# In[39]:


df.ix[1,1]


# In[40]:


df.ix['2017-06-01':'2017-06-05']


# In[41]:


df.ix['2017-06-05','open']


# In[42]:


df.ix[1,'open']


# In[43]:


df.ix['2017-06-01',0]


# In[46]:


df[df.open > 8.12]


# In[49]:


df[(df.open >8.9) & (df.close < 9.17)]


# In[50]:


df[df>10]


# In[51]:


df[df > 9.] = 0


# In[52]:


df


# In[53]:


df[df['high'].isin([0.00,9.00])]


# In[55]:


panel = get_price(['000001.XSHE','000002.XSHE'], '2017-06-01','2017-06-14','1d',fields=['open','high','low','close'])
panel


# In[56]:


panel['open',:,:]


# In[57]:


panel[:,'2017-06-01',:]


# In[59]:


panel[:,:,'000001.XSHE']


# In[60]:


df = get_price('000001.XSHE','2017-06-01','2017-06-14','1d',fields=['open','high','low','close'])
df = df[df > 9.0]
df


# In[62]:


df.dropna()


# In[63]:


df.fillna(value=0)


# In[64]:


pd.isnull(df)


# In[65]:


df.mean()


# In[66]:


df.mean(1)


# In[67]:


df.mean(axis = 1, skipna = False)


# In[70]:


df1 = get_price('000001.XSHE','2017-06-01','2017-06-14','1d',['open','high','low','close'])
df1


# In[71]:


df2 = get_price('000001.XSHE','2017-05-15','2017-05-31','1d',['open','high','low','close'])
df2


# In[72]:


pd.concat([df1,df2],axis=0)


# In[73]:


pd.concat([df1,df2], axis=1)


# In[74]:


df1


# In[76]:


s = df1.iloc[0]
s


# In[77]:


df1.append(s,ignore_index=False)


# In[78]:


df1.append(s, ignore_index=True)


# In[79]:


z = df1.append(s, ignore_index=False)
z


# In[80]:


z.duplicated()

