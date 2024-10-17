def transform_variables(df, short_code_mapping):

    def get_short_code(var_id):
        return short_code_mapping.get(str(var_id), f"var_{var_id}")

    df['short_code'] = df['idVariable'].apply(get_short_code)

    # Reordenamiento de columnas
    df = df[["idVariable", "cdSerie", "short_code", "descripcion", "fecha", "valor"]]

    return df
