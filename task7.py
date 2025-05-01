#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install mysql-connector-python')


# In[3]:


get_ipython().system('pip install ipython-sql')


# In[4]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[5]:


get_ipython().system('pip install PyMySQL')


# In[37]:


import pymysql
import mysql.connector
import pandas as pd


# In[38]:


db_name="sales_order"
db_host="localhost"
db_username="root"
db_password="password"
try:
    conn=pymysql.connect(host=db_host,port=int(3306),
                         user="root",password=db_password,
                        db=db_name)
except e:
    print(e)
if conn:
    print("Connection successful")
else: 
    print("error")


# In[39]:


df=pd.read_sql_query("select *From sales_tab1",conn)


# In[40]:


df


# In[41]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[32]:


get_ipython().system('pip install duckdb')


# In[42]:


import duckdb
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('config', 'SqlMagic.autopandas=True')
get_ipython().run_line_magic('sql', 'duckdb:///:memory:')


# In[43]:


get_ipython().run_cell_magic('sql', '', 'select *From sales_tab1')


# In[44]:


df.describe()


# In[14]:


df.info()


# In[17]:


df["location"]=df["location"].astype("string")
df["product"]=df["product"].astype("string")
df["sales_channel"]=df["sales_channel"].astype("string")


# In[18]:


df.info()


# In[19]:


df["ship_date"]=pd.to_datetime(df['ship_date'], infer_datetime_format=True)


# In[20]:


df.info()


# In[21]:


import matplotlib.pyplot as plt
import numpy as np


# In[45]:


df1=pd.read_sql_query("select product, sum(quantity) as total_quantity, sum(quantity*unit_cost) as revenue from sales_tab1 group by product;",conn)


# In[46]:


df1


# In[48]:


df1.plot(kind="bar",x="product",y="revenue")


# In[ ]:




