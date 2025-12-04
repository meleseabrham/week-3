from abc import ABC, abstractmethod
import pandas as pd

class IDataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path: str) -> pd.DataFrame:
        pass

class IPlotter(ABC):
    @abstractmethod
    def plot_distribution(self, data: pd.DataFrame, column: str):
        pass

    @abstractmethod
    def plot_scatter(self, data: pd.DataFrame, x_col: str, y_col: str):
        pass

    @abstractmethod
    def plot_boxplot(self, data: pd.DataFrame, column: str):
        pass

    @abstractmethod
    def plot_bar(self, data: pd.DataFrame, x_col: str, y_col: str, title: str):
        pass

    @abstractmethod
    def plot_time_series(self, data: pd.DataFrame, date_col: str, value_cols: list):
        pass
