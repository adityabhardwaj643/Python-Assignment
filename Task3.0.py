#

import pandas as pd


def load_and_display_csv(file_path):
    df = pd.read_csv(file_path)
    print("First few rows of the DataFrame:")
    print(df.head())


file_path = 'data.csv'  # Replace with your CSV file path
load_and_display_csv(file_path)