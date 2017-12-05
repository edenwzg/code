
# coding: utf-8

# In[18]:


import matplotlib.pyplot as plt
import numpy as np


# In[4]:


x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x*2))
plt.show()


# In[20]:


x


# In[21]:


help(np.linspace)


# In[6]:


plt.plot(x, np.sin(x),
        x, np.sin(2 * x))
plt.show()


# In[8]:


plt.plot(x, np.sin(x), 'b-X',
        x, np.cos(x), 'g--')
plt.show()


# ## 使用子图

# In[29]:


plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), 'r')
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'bo')
plt.show()


# In[28]:


y = np.sin(x)
plt.scatter(x, y)
plt.show()


# In[56]:


x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 100
colour = np.random.rand(1000)
plt.scatter(x, y, size, colour)
plt.colorbar()
plt.show()


# In[58]:


x = np.random.randn(1000)
plt.hist(x, 50)
plt.show()


# In[47]:


x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
plt.legend()
plt.xlable('Rads')
plt.ylable('Amplitude')
plt.title('Sin and Cos Waves')
plt.show()

