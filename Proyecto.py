
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv('banknote.csv')
data


# In[92]:


import numpy as np
import matplotlib.pyplot as plt
plt.xlabel('V1')
plt.ylabel('V1')
plt.scatter(data['V1'], data['V2'], mean*10, alpha=.25)

import matplotlib.patches as patches
fig,plot = plt.subplots()

plot.scatter(data['V1'], data['V2'], alpha=.4)
#plt.yticks(np.arange(-15, 15, 5)) 
#plt.xticks(np.arange(-10, 15, 5)) 
#plt.vlines(V1M, 15, -15, linestyles ="dashed", colors ="r", label='V1')
#plt.hlines(V2M, 15, -15, linestyles ="dashed", colors ="r")
plt.xlabel('V1')
plt.ylabel('V2')
#plt.legend('vmm')

mean1=np.mean(data)
print(mean)

stdv=np.std(data)
plot.scatter(stdv['V1'], stdv['V2'], s=1000, color='b')
stdv
plot.scatter(mean['V1'], mean['V2'], s=1000, color='r')
plot.legend('vmm')


# In[104]:


import matplotlib.patches as patches
fig,plot = plt.subplots()
plot.scatter(data['V1'], data['V1'], alpha=.4)
plot.scatter(data['V2'], data['V2'], s=1, alpha=.1)

