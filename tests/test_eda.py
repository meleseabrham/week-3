import pytest
import pandas as pd
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.application.eda_service import EDAService
from src.infrastructure.csv_loader import CSVLoader
from src.infrastructure.plotting import MatplotlibPlotter

class MockPlotter(MatplotlibPlotter):
    def plot_distribution(self, data, column):
        pass
    def plot_scatter(self, data, x_col, y_col):
        pass
    def plot_boxplot(self, data, column):
        pass
    def plot_bar(self, data, x_col, y_col, title):
        pass
    def plot_time_series(self, data, date_col, value_cols):
        pass

class MockLoader(CSVLoader):
    def load_data(self, file_path: str) -> pd.DataFrame:
        data = {
            'PolicyID': ['P001', 'P002'],
            'TransactionMonth': ['2014-01-01', '2014-01-01'],
            'TotalPremium': [1000, 1200],
            'TotalClaims': [0, 500],
            'Province': ['Gauteng', 'Western Cape'],
            'VehicleType': ['Sedan', 'SUV'],
            'Gender': ['Male', 'Female']
        }
        return pd.DataFrame(data)

def test_eda_service_initialization():
    loader = MockLoader()
    plotter = MockPlotter()
    service = EDAService(loader, plotter)
    assert service is not None

def test_perform_initial_analysis():
    loader = MockLoader()
    plotter = MockPlotter()
    service = EDAService(loader, plotter)
    
    # Run analysis on dummy path (loader is mocked)
    df = service.perform_initial_analysis("dummy.csv")
    
    assert df is not None
    assert not df.empty
    assert 'LossRatio' not in df.columns # Loss ratio is calculated but not added to main df in current impl
    assert df['TotalPremium'].sum() == 2200
