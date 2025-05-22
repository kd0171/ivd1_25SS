import pandas as pd

def load_and_clean_data(path, save_to=None):
    df = pd.read_csv(path)
    df = df.dropna()
    if save_to:
        df.to_csv(save_to, index=False)
    return df
