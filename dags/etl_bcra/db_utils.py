import os
import pandas as pd
from sqlalchemy import create_engine

default_connection_string = 'postgresql+psycopg2://airflow:airflow@postgres:5432/airflow'

connection_string = os.getenv('SQL_ALCHEMY_CONN', default_connection_string)

engine = create_engine(connection_string)


def load_table(df, table_name):
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    print(f"Data uploaded successfully to {table_name}!")


def read_table(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, con=engine)
    return df
