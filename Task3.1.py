import pandas as pd

# Function to calculate and display basic statistics
def display_basic_statistics(file_path):
    df = pd.read_csv(file_path)
    print("Basic Statistics:")
    print("Mean:")
    print(df.mean(numeric_only=True))
    print("Median:")
    print(df.median(numeric_only=True))
    print("Mode:")
    print(df.mode(numeric_only=True).iloc[0])

# Example usage
file_path = 'data.csv'  
display_basic_statistics(file_path)
