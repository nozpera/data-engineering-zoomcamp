#!/usr/bin/env python
# coding: utf-8

import pandas as pd

import psycopg2

from time import time

from sqlalchemy import create_engine

engine = create_engine('postgresql://Postgres:Postgres@localhost:5431/ny_taxi')

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