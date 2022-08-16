
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv('banknote.csv')
data


# In[3]:


#1)tamaño 1372 x 2
#2) 2 entidades: V1 y V2


# In[4]:


import numpy as np
mean= np.mean(data)
mean


# In[5]:


print(np.max(data),np.min(data))


# In[6]:


std_desv= np.std(data)
std_desv


# In[8]:


import matplotlib.pyplot as plt
plt.xlabel('V1')
plt.ylabel('V2')
plt.scatter(data['V1'], data['V2'])


# In[89]:


V1=data['V1']
V2=data['V2']
V1M=np.mean(data['V1'])
V2M=np.mean(data['V2'])
V1D=np.std(data['V1'])
V2D=np.std(data['V2'])

from sklearn.cluster import KMeans
VV= np.column_stack((V1, V2))
km_res = KMeans(n_clusters=3).fit(VV)
clusters=km_res.cluster_centers_
plt.scatter(data['V1'], data['V2'])
plt.scatter(clusters[:,0], clusters[:,1], s=2000, alpha=0.9)
plt.xlabel('V1')
plt.ylabel('V2')


import matplotlib.patches as patches

ellipse = patches.Ellipse([V1M, V2M], V1D*2, V2D*2, alpha=1, edgecolor='r',fc='None', lw=2)
fig,graph = plt.subplots()

graph.scatter(data['V1'], data['V2'])
plt.yticks(np.arange(-15, 15, 5)) 
plt.xticks(np.arange(-10, 15, 5)) 
graph.add_patch(ellipse)
plt.xlabel('V1')
plt.ylabel('V2')
plt.rcParams["figure.figsize"] = 14, 4
plt.legend('s')


import matplotlib.patches as patches
fig,plot = plt.subplots()

plot.scatter(data['V1'], data['V2'])
plt.yticks(np.arange(-15, 15, 5)) 
plt.xticks(np.arange(-10, 15, 5)) 
plt.vlines(V1M, 15, -15, linestyles ="dashed", colors ="r", label='V1')
plt.hlines(V2M, 15, -15, linestyles ="dashed", colors ="r")
plt.xlabel('V1')
plt.ylabel('V2')
plt.legend('vmm')


# In[87]:


import matplotlib.patches as patches

ellipse = patches.Ellipse([V1M, V2M], V1D*2, V2D*2, alpha=1, edgecolor='r',fc='None', lw=2, label='area')
fig,graph = plt.subplots()

graph.scatter(data['V1'], data['V2'])
plt.yticks(np.arange(-15, 15, 5)) 
plt.xticks(np.arange(-10, 15, 5)) 
graph.add_patch(ellipse)
plt.xlabel('V1')
plt.ylabel('V2')
plt.rcParams["figure.figsize"] = 14, 4
graph.legend('S',bbox_to_anchor=(0.5,-0.2), loc="upper center", fancybox=True, shadow=True, ncol=0)

