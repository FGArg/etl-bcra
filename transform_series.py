from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError, NoSuchTableError

def transform_series(df_new_series):
    
    # SQLite engine
    connection_string = 'sqlite:///local_database.db'
    engine = create_engine(connection_string)

    try:
        
        query = 'SELECT * FROM bcra_series'
        df_actual_series = pd.read_sql_query(query, con=engine)

        
        if df_actual_series.empty:
            print("No records found in bcra_series. Using new data only.")
            df_updated_series = df_new_series.copy()
            
        else:
            # Registros anteriores
            df_old_series = df_actual_series[~df_actual_series['fecha'].isin(df_new_series['fecha'])]

            # Combinación de registros anteriores y nuevos registros
            df_updated_series = pd.concat([df_old_series, df_new_series], ignore_index=True)

            # Sanity check: eliminación de duplicados
            df_updated_series = df_updated_series.drop_duplicates(subset='fecha', keep='last')

            # Ordenamiento cronológico
            df_updated_series = df_updated_series.sort_values('fecha').reset_index(drop=True)

        return df_updated_series

    except SQLAlchemyError as e:
        print(f"[Warning] Error accessing bcra_series table: {e}")
        return df_new_series

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
