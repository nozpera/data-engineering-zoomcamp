#!/usr/bin/env python
# coding: utf-8

import pandas as pd

import psycopg2

import argparse

import requests

from time import time

from sqlalchemy import create_engine

def download_file(url, output):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(output, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully: {output}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        raise

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = 'output.csv'

    download_file(url, csv_name)
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    t_start = time()
    df = pd.read_csv(csv_name, delimiter=',')
    df.to_sql(table_name, con=engine, if_exists='append')
    t_end = time()
    print(f'Completed! Total time taken was {t_end-t_start:10.3f}')

# user, password, host, port, database name, table name, url of the csv file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data into Postgres')

    parser.add_argument('--user', required=True, help='username for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table-name', required=True, help='table name for postgres')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)