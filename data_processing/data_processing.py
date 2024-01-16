import pandas as pd

def read_data(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    df['activity_date'] = pd.to_datetime(df['activity_date'], format='%d/%m/%Y')
    return df

def clean_data(df):
    df_cleaned = df.dropna()
    product_counts = df_cleaned['product'].value_counts()
    products_to_remove = product_counts[product_counts == 1].index
    df_cleaned = df_cleaned[~df_cleaned['product'].isin(products_to_remove)]
    df_cleaned.reset_index(drop=True, inplace=True)
    return df_cleaned