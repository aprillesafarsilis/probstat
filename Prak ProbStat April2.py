#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 2, -5, 0.3, 6, -2, 4]  # numeric vector
b = ["one", "two", "three"]     # character vector
c = [True, True, True, False, True]  # logical vector
print(a)
print(b)
print(c)


# In[2]:


#MATRIKS
import numpy as np
cells = [3, 15, -27, 38]
r_nama = ["R1", "R2"]
c_nama = ["C1", "C2"]
april_matrix = np.matrix(cells).reshape(2, 2)
print(april_matrix)


# In[3]:


import pandas as pd
import numpy as np

april1 = [1, 2, 3, 4]
april2 = ["red", "white", "red", np.nan]  # Menggunakan np.nan untuk merepresentasikan NA
april3 = [True, True, True, False]

data_april = pd.DataFrame({'ID': april1, 'Color': april2, 'Passed': april3})
print(data_april)


# In[4]:


import pandas as pd

data_april = pd.DataFrame({'id': list('abcdefghij'), 'x': list(range(1, 11)), 'y': list(range(11, 21))})
print(data_april)


# In[5]:


pip install mysql-connector-python


# In[6]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="houseprices2"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM april_houseprices;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[7]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['Brick'] == 'No']

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[8]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kondisi yang kompleks
df_filtered = df[(df['Brick'] == 'No') | (df['Neighborhood'] == 'East')]

# Menampilkan hasil filter
print(df_filtered)


# In[9]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ps2[april]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM data_april;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[10]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[(df['Gender'] == 'L')]

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[ ]:




