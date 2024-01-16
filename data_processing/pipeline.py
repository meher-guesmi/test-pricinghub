from .data_processing import *

def main_pipeline(calculation_type, percent_threshold, euro_threshold):
    file_path = r".\data.csv"

    df = read_data(file_path)

    df_cleaned = clean_data(df)

    results = calculate_price_difference(df_cleaned, calculation_type, percent_threshold, euro_threshold)

    return results