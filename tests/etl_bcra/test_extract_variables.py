from dags.etl_bcra.extract_variables import extract_variables

def test_extract_variables():
    # Set up
    expected_output_columns = ['idVariable', 'cdSerie', 'descripcion', 'fecha', 'valor']
    
    # Action
    actual_output = extract_variables()
    actual_output_columns = actual_output.columns.tolist()
    
    # Assert
    assert actual_output_columns == expected_output_columns, f"Expected columns: {expected_output_columns}, but got: {actual_output_columns}"
