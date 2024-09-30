import requests
import pandas as pd
from datetime import datetime, timedelta


def extract_series(df_variables):

    # start_date: hace 365 días | end_date: hoy
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.today().strftime('%Y-%m-%d')

    dfs = []

    for index, row in df_variables.iterrows():
        id_variable = row['idvariable']
        short_code = row['short_code']

        url = f'https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable/{id_variable}/{start_date}/{end_date}'

        print(f"Fetching data for variable ID: {id_variable}")

        response = requests.get(url, verify=False)

        data = response.json()
        df = pd.DataFrame(data['results'])

        # Renombramos la columna con el short_code de la variable
        df = df[['fecha', 'valor']].rename(columns={'valor': short_code})

        dfs.append(df)

    # Merge del dataframe
    df_merged = dfs[0]
    for df in dfs[1:]:
        df_merged = pd.merge(df_merged, df, on='fecha', how='outer')

    # Ordenamiento cronológico
    df_pivot = df_merged.sort_values('fecha').reset_index(drop=True)

    return df_pivot
