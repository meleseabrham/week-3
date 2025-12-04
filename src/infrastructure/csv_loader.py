import pandas as pd
from src.application.interfaces import IDataLoader

class CSVLoader(IDataLoader):
    def load_data(self, file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error loading CSV: {e}")
            raise
