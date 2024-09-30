import pandas as pd


def transform_series(df_actual_series, df_new_series):

    if df_actual_series is None:
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
