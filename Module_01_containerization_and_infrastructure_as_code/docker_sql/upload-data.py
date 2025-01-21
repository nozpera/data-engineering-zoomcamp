#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[15]:


import psycopg2


# In[16]:


from time import time


# In[22]:


from sqlalchemy import create_engine


# In[17]:


pd.__version__


# In[18]:


df = pd.read_csv('./dataset/yellow_tripdata_2021-01.csv', delimiter=',', nrows=100)


# In[21]:


df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])


# In[23]:


engine = create_engine('postgresql://Postgres:Postgres@localhost:5431/ny_taxi')


# In[24]:


engine.connect()


# In[25]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[26]:


df_iter = pd.read_csv('./dataset/yellow_tripdata_2021-01.csv', delimiter=',', iterator=True, chunksize=100000)

count = 0
t_start = time()

for batch_df in df_iter:
    count += 1
    print(f'inserting batch {count}...')
    b_start = time()

    batch_df['tpep_pickup_datetime'] = pd.to_datetime(batch_df['tpep_pickup_datetime'])
    batch_df['tpep_dropoff_datetime'] = pd.to_datetime(batch_df['tpep_dropoff_datetime'])
    batch_df.to_sql('yellow_taxi_data', con=engine, if_exists='append')
    
    b_end = time()

    print(f"inserted! time taken {b_end - b_start:10.3f} seconds.\n")

t_end = time()
print(f'Completed! Total time taken was {t_end-t_start:10.3f} seconds for {count} batches.')

