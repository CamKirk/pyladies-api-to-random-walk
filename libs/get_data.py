import requests
import pandas as pd
from config import quandl_key

def get_data(ticker_symbol):
    url = f"https://www.quandl.com/api/v3/datasets/WIKI/{ticker_symbol}/data.json"
    params = {
        "api_key":quandl_key
    }

    res = requests.get(url, params=params)
    
    dataset = res.json()['dataset_data']
    
    column_names = dataset['column_names']
    values = dataset['data']
    
    df = pd.DataFrame(values, columns=column_names)
    
    return df