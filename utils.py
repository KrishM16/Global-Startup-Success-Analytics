# utils.py

import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df.dropna(subset=['Funding Amount', 'Sector', 'Country'], inplace=True)
    df.drop_duplicates(inplace=True)
    df['Number of Founders'] = df['Founders'].apply(lambda x: len(str(x).split(',')))
    return df
