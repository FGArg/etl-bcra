from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

def load_table(df, table_name):
    
    # SQLite engine
    connection_string = 'sqlite:///local_database.db'
    engine = create_engine(connection_string)

    try:
        df.to_csv(f"./data/{table_name}.csv", index=False)
        df.to_sql(name=f"{table_name}", con=engine, if_exists='replace', index=False)
        print("Data uploaded successfully!")
    except SQLAlchemyError as e:
        print(f"Error uploading data to database: {e}")
