import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)

    print("\n Loaded Data")
    print(df)

    print("\n Dataset Information:")
    print(df.info())

    return df