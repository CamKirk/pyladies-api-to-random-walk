import requests
import pandas as pd
from config import quandl_key # this file doesn't exist and you need to make it yourself!

def get_data(ticker_symbol):
    """User-defined function to GET data using the Quandl API
        
    
    Returns:
        dataframe () containing OHLC and Adj. OHLC info
    
    """
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