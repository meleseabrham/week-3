from src.application.interfaces import IDataLoader, IPlotter
import pandas as pd

class EDAService:
    def __init__(self, data_loader: IDataLoader, plotter: IPlotter):
        self.data_loader = data_loader
        self.plotter = plotter

    def perform_initial_analysis(self, file_path: str):
        df = self.data_loader.load_data(file_path)
        print(f"Loaded data with shape: {df.shape}")
        
        # Clean column names
        df.columns = df.columns.str.strip()
        
        # Data Cleaning & Conversion
        try:
            df['TotalPremium'] = pd.to_numeric(df['TotalPremium'], errors='coerce')
            df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')
            if 'TransactionMonth' in df.columns:
                df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
        except Exception as e:
            print(f"Error cleaning data: {e}")
            raise

        # 1. Overall Loss Ratio
        total_premium = df['TotalPremium'].sum()
        total_claims = df['TotalClaims'].sum()
        loss_ratio = total_claims / total_premium if total_premium > 0 else 0
        print(f"Overall Loss Ratio: {loss_ratio:.2%}")

        # 2. Loss Ratio by Categories
        print("Analyzing Loss Ratio by Categories...")
        for col in ['Province', 'VehicleType', 'Gender']:
            if col in df.columns:
                group = df.groupby(col)[['TotalPremium', 'TotalClaims']].sum()
                group['LossRatio'] = group['TotalClaims'] / group['TotalPremium']
                print(f"\nLoss Ratio by {col}:\n{group['LossRatio']}")
                self.plotter.plot_bar(group.reset_index(), col, 'LossRatio', f'Loss Ratio by {col}')

        # 3. Temporal Trends
        if 'TransactionMonth' in df.columns:
            print("\nAnalyzing Temporal Trends...")
            monthly = df.groupby('TransactionMonth')[['TotalPremium', 'TotalClaims']].sum().reset_index()
            self.plotter.plot_time_series(monthly, 'TransactionMonth', ['TotalPremium', 'TotalClaims'])

        # 4. Outliers
        print("\nGenerating Outlier Plots...")
        self.plotter.plot_boxplot(df, 'TotalClaims')
        self.plotter.plot_boxplot(df, 'TotalPremium')

        return df
