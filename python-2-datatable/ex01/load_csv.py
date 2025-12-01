import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Writes dimensions of the given data set and returns it"""
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
