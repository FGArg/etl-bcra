import pandas as pd

SHORT_CODE_MAPPING = {
    1: 'res_int',           # Reservas Internacionales
    4: 'tc_min',            # Tipo de Cambio Minorista
    5: 'tc_may',            # Tipo de Cambio Mayorista
    6: 'tasa_pmonet',       # Tasa de Política Monetaria
    7: 'tasa_badlar',       # Tasa BADLAR
    8: 'tasa_tm20',         # Tasa TM20
    9: 'tasa_pase_act',     # Tasa Pases Activos
    10: 'tasa_pase_pas',    # Tasa Pases Pasivos
    11: 'tasa_baibar',      # Tasa Préstamos entre entidades
    12: 'tasa_depo_30d',    # Depósitos a 30 días
    13: 'tasa_lend',        # Préstamos por adelantos
    14: 'tasa_pers',        # Préstamos personales
    15: 'base_mon',         # Base Monetaria
    16: 'circ_mon',         # Circulación Monetaria
    17: 'bil_pub',          # Billetes y monedas en poder del público
    18: 'efec_fin',         # Efectivo en entidades financieras
    19: 'dep_bcr',          # Depósitos en el BCRA
    21: 'dep_fin',          # Depósitos en efectivo
    22: 'dep_ccte',         # En cuentas corrientes
    23: 'dep_ahorro',       # En Caja de ahorros
    24: 'dep_plazo',        # A plazo
    25: 'm2_priv',          # M2 privado
    26: 'pr_sec_priv',      # Préstamos al sector privado
    27: 'infl_mens',        # Inflación mensual
    28: 'infl_interan',     # Inflación interanual
    29: 'infl_esp',         # Inflación esperada
    30: 'cer',              # CER
    31: 'uva',              # UVA
    32: 'uvi',              # UVI
    34: 'tasa_pmonet_ea',   # Tasa de Política Monetaria e.a.
    35: 'tasa_badlar_ea',   # BADLAR e.a.
    40: 'icl',              # Índice para Contratos de Locación
    41: 'tasa_pase_pas_ea', # Pases Pasivos e.a.
    42: 'pases_pas',        # Pases pasivos
    43: 'tasa_just'         # Tasa para uso de la Justicia
}


def transform_variables(df):
    
    def get_short_code(var_id):
        return SHORT_CODE_MAPPING.get(var_id, f"var_{var_id}")
    
    df['short_code'] = df['idVariable'].apply(get_short_code)
    
    # Reordenamiento de columnas
    df = df[["idVariable", "cdSerie", "short_code", "descripcion", "fecha", "valor"]]

    
    return df
