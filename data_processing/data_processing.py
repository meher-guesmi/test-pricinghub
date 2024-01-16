import pandas as pd

def read_data(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    df['activity_date'] = pd.to_datetime(df['activity_date'], format='%d/%m/%Y')
    return df
