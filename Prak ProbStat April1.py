#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd

# Membuat dataframe dari data yang disalin ke clipboard
df = pd.read_clipboard()
 
# Menampilkan DataFrame
print(df)


# In[28]:


df


# In[29]:


# Menghitung rata-rata tinggi
rata_tinggi = df['Tinggi Badan'].mean()
rata_tinggi


# In[30]:


print(df.dtypes)


# In[31]:


# Mengubah tipe data kolom 'Angkatan' menjadi string
df['Angkatan'] = df['Angkatan'].astype(str)


# In[32]:


print(df.dtypes)


# In[10]:


df = pd.read_csv("data_april.csv")
df


# In[33]:


df = pd.read_excel("data_april.xlsx")
df


# In[36]:


data_nama = pd.read_csv("PrakStatistika\data_april.csv")
print(data_nama)


# In[ ]:





# In[ ]:





# In[ ]:




