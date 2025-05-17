import pandas as pd

def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

