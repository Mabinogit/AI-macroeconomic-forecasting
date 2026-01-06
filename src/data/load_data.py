import pandas as pd

def load_inflation_data(file_path="data/raw/inflation.csv"):
    """
    Loads the raw inflation CSV into a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    print(f"Loaded data with {df.shape[0]} rows and {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    df = load_inflation_data()
    print(df.head())
