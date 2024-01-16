from .data_processing import *

def main_pipeline(calculation_type, percent_threshold, euro_threshold):
    """This is the main pipeline to read data and calculate the price difference based on thresholds

    Args:
        calculation_type (string): Type of calculation, either "last_two_dates" or "first_last_dates"
        percent_threshold (float): Percentage threshold for price difference
        euro_threshold (float): Euro threshold for price difference

    Returns:
        dict: A dictionary with product id as key and price difference as value
    """
    file_path = r".\data.csv"

    df = read_data(file_path)

    df_cleaned = clean_data(df)

    results = calculate_price_difference(df_cleaned, calculation_type, percent_threshold, euro_threshold)

    return results