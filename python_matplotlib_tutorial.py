
# coding: utf-8

# In[4]:


from matplotlib import pyplot as plt


# In[5]:


plt.plot([1,2,3],[4,5,1])


# In[8]:


plt.plot([22,33,11],[11,21,13])


# In[9]:


x=[5,8,10]
y=[12,16,6]
plt.plot(x,y)
plt.title('info')
plt.ylabel('y-axis')
plt.xlabel('x-axis')


# In[11]:


from matplotlib import pyplot as plt


# In[13]:


from matplotlib import style


# In[14]:


style.use('ggplot')

x=[5,8,10]
y=[12,16,6]

x2=[6,9,11]
y2=[6,15,7]

plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'c',label='linetwo',linewidth=5)

plt.title('epic info')
plt.ylabel("y-axis")
plt.xlabel("x-axis")

plt.legend()
plt.grid(True,color='k')


# In[15]:


import matplotlib.pyplot as plt


# In[17]:


plt.bar([1,3,5,7,9],[5,2,7,8,2],label='Example one')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='Example two',color='g')

plt.legend()

plt.ylabel("bar height")
plt.xlabel("bar height")

plt.title("My first plot bar graph")


# In[19]:


population_ages=[22,55,62,45,21,22,34,42,4,99,102,110,120,121,122,130,111,
                 115,112,80,75,65,54,44,43,42,48]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.legend()


# In[20]:


x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='skitscat',color='k',s=25,marker='o')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()


# In[24]:


days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()


# In[25]:


slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
       labels=activities,
       colors=cols,
       startangle=90,
       shadow=True,
       explode=(0,0.1,0,0),
       autopct='%1.1f%%')
plt.title('Pie Plot')


# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[6]:


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()

