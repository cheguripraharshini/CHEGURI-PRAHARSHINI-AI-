#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print("Praharshini")


# # variable programs

# In[3]:


name = "PANDU"
age = 20
income = 15000


# In[4]:


print(name)
print(age)
print(income)


# In[6]:


namelist = "pandu" , "abhi"
namelist


# In[8]:


name_list = "abhi" , "pandu"
name_list


# In[9]:


type("ai")


# In[10]:


name = "ai"
type(name)


# In[11]:


x=10
type(x)


# In[12]:


x=10.7
type(x)


# In[14]:


x=True
type(x)


# In[15]:


y=False
type(y)


# In[16]:


z="true"
type(z)


# # LIST

# In[6]:


samplelist = [1,2,3,7,-1,"hi",5.7,1,1,1]
samplelist


# In[7]:


type(samplelist)


# In[11]:


samplelist[4]


# In[14]:


samplelist[-1]


# In[16]:


samplelist[0]=100
samplelist


# # TUPLE

# In[17]:


sample_tuple = (1,6,2.3,8.3,"hi")
sample_tuple


# In[18]:


type(sample_tuple)


# In[19]:


sample_tuple2 = 1,6,2.3,8.3,"hi"
sample_tuple2


# In[20]:


type(sample_tuple2)


# In[21]:


print(sample_tuple)
print(sample_tuple2)


# In[23]:


sample_tuple[1]


# # DAY -2 

# SET

# In[24]:


sample_set = {1,2,3,4,5,1,13.4,9.6,"hi","hello","ds",-1,11.4,21.5}
sample_set


# In[25]:


sample_set.add(100)
sample_set


# In[27]:


sample_set.remove(-1)
sample_set


# DICTIONARY

# In[35]:


dict_1 = {'name':"PANDU","hobbies":['painting','singing','reading books'],1:20}
dict_1.keys()


# In[31]:


dict_1.values()


# In[32]:


dict_1['name'] = "ABHI"
dict_1


# In[33]:


del dict_1["name"]
dict_1


# In[39]:


dict_1.update({"class":"ds"})
dict_1


# In[40]:


len(dict_1)

