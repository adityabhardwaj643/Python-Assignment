
import pandas as pd


def filter_dataframe(file_path, column, condition):
    df = pd.read_csv(file_path)
    filtered_df = df[df[column] == condition]
    print("Filtered DataFrame:")
    print(filtered_df)

# Example usage
file_path = 'data.csv'   
column = 'Occupation'  
condition = 'Engineer'  
filter_dataframe(file_path, column, condition)
