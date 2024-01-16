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

def calculate_price_difference(df_clean, calculation_type, percent_threshold, euro_threshold):
    results = {}

    for product_id, group in df_clean.groupby('product'):
        reference_index = -2 if calculation_type == 'last_two_dates' else 0

        price_diff = int(group['price'].iloc[-1] - group['price'].iloc[reference_index])

        if (
            abs(price_diff) >= euro_threshold
            or abs(price_diff) >= group['price'].iloc[reference_index] * percent_threshold / 100
        ):
            results[product_id] = price_diff

    return results