import requests
import pandas as pd


def extract_variables():
    
    url = "https://api.bcra.gob.ar/estadisticas/v2.0/principalesvariables"
    
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        
        data = response.json()
        new_df = pd.DataFrame(data['results'])
        
        return new_df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

