#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import os
import pandas as pd
import plotly.graph_objects as go


# In[41]:


df = pd.read_csv('multifield.0030.txt', sep=" ", header=None,skiprows=600*248*100, nrows=600*248*5) #z=100 to z=104


# In[42]:


df


# In[43]:


df[4].describe() #He mass abundance


# In[44]:


values = np.array(df[4])


# In[45]:


x=[]
y=[]
z=[]
for k in range(5):
    for j in range(248):
        for i in range(600):
            x.append(i)
            y.append(j)
            z.append(k)


# In[46]:


#isosurfaces
fig = go.Figure(data=go.Isosurface(
    x=x,
    y=y,
    z=z,
    value=values.flatten(),
    isomin=0.000053,
    isomax=0.240000,
    surface_count=5, # number of isosurfaces, 5 
    colorbar_nticks=5, # colorbar ticks correspond to isosurface values
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()


# In[48]:


#opacity experiment
#isosurfaces
fig = go.Figure(data=go.Isosurface(
    x=x,
    y=y,
    z=z,
    value=values.flatten(),
    opacity=0.6,
    isomin=0.000053,
    isomax=0.240000,
    surface_count=5, # number of isosurfaces, 5 
    colorbar_nticks=5, # colorbar ticks correspond to isosurface values
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()


# In[ ]:




