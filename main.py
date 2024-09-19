from extract_variables import extract_variables
from transform_variables import transform_variables

from extract_series import extract_series
from transform_series import transform_series

from load_table import load_table


def main():
    
    variables_df = extract_variables()
    
    if variables_df is not None:
        variables_df = transform_variables(variables_df)
        load_table(variables_df, "bcra_principales_variables")
        
        series_df = extract_series(variables_df)
    
        if series_df is not None:
            series_df = transform_series(series_df)
            load_table(series_df, "bcra_series")
    

if __name__ == "__main__":
    main()
