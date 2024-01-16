import pandas as pd

def read_data(file_path):
    """This function read csv file as Dataframe

    Args:
        file_path (string): Path to csv file

    Returns:
        _type_: pandas.DataFrame
    """    
    df = pd.read_csv(file_path, delimiter=";")
    df['activity_date'] = pd.to_datetime(df['activity_date'], format='%d/%m/%Y')
    return df

def clean_data(df):
    """This function clean the dataframe

    Args:
        df (pandas.DataFrame): The Raw Dataframe

    Returns:
        pandas.DataFrame: The DataFrame after cleaning
    """    
    df_cleaned = df.dropna()
    product_counts = df_cleaned['product'].value_counts()
    products_to_remove = product_counts[product_counts == 1].index
    df_cleaned = df_cleaned[~df_cleaned['product'].isin(products_to_remove)]
    df_cleaned.reset_index(drop=True, inplace=True)
    return df_cleaned

def calculate_price_difference(df_clean, calculation_type, percent_threshold, euro_threshold):
    """This function calculate the price difference based on a calculation type
        and return the products that their price difference is greater than one the thresholds

    Args:
        df_clean (pandas.DataFrame): Cleaned DataFrame
        calculation_type (string): Type of calculation, either "last_two_dates" or "first_last_dates"
        percent_threshold (float): Percentage threshold for price difference
        euro_threshold (float): Euro threshold for price difference

    Returns:
        dict: A dictionary with product id as key and price difference as value
    """    
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