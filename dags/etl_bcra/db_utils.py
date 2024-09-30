from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

default_connection_string = 'postgresql+psycopg2://airflow:airflow@postgres:5432/airflow'

connection_string = os.getenv('SQL_ALCHEMY_CONN', default_connection_string)

engine = create_engine(connection_string)

db_schema = os.getenv('POSTGRES_DB_SCHEMA', '')


def load_table(df, table_name):
    df.columns = df.columns.str.lower()
    df.to_sql(name=table_name, con=engine, schema=db_schema, if_exists='replace', index=False)
    print(f"Data uploaded successfully to {db_schema}.{table_name}!")


def read_table(table_name):
    query = f'SELECT * FROM "{db_schema}"."{table_name}"'
    df = pd.read_sql(query, con=engine)
    return df
