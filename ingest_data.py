#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse

def main(params):
    user = params.user
    pw = params.pw
    host = params.host
    db = params.db
    table = params.table
    url = params.url
    port = params.port


    engine = create_engine(f'postgresql://{user}:{pw}@{host}:{port}/{db}')

    #read data from url
    df = pd.read_parquet(url)

    #assign headers
    df.head(n=0).to_sql(name=table, con=engine, if_exists='replace')

    #to sql with postgres con
    df.to_sql(  
        name=table, 
        con=engine, 
        if_exists='append', 
        chunksize=250000
        )

####################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ingest parquet data to postgres')
    
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--pw', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table', help='name of the table to write results to')
    parser.add_argument('--url', help='url of the parquet file')
    

    args = parser.parse_args()

    main(args)






