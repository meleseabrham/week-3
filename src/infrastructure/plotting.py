import matplotlib.pyplot as plt
import seaborn as sns
import os
from src.application.interfaces import IPlotter

class MatplotlibPlotter(IPlotter):
    def plot_distribution(self, data, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column].dropna(), kde=True)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        os.makedirs('reports/figures', exist_ok=True)
        plt.savefig(f'reports/figures/dist_{column}.png')
        plt.close()

    def plot_scatter(self, data, x_col, y_col):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x=x_col, y=y_col)
        plt.title(f"{x_col} vs {y_col}")
        os.makedirs('reports/figures', exist_ok=True)
        plt.savefig(f'reports/figures/scatter_{x_col}_{y_col}.png')
        plt.close()

    def plot_boxplot(self, data, column):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=data[column].dropna())
        plt.title(f"Boxplot of {column}")
        os.makedirs('reports/figures', exist_ok=True)
        plt.savefig(f'reports/figures/box_{column}.png')
        plt.close()

    def plot_bar(self, data, x_col, y_col, title):
        plt.figure(figsize=(12, 6))
        sns.barplot(data=data, x=x_col, y=y_col)
        plt.title(title)
        plt.xticks(rotation=45)
        os.makedirs('reports/figures', exist_ok=True)
        plt.savefig(f'reports/figures/bar_{title.replace(" ", "_")}.png')
        plt.close()

    def plot_time_series(self, data, date_col, value_cols):
        plt.figure(figsize=(14, 7))
        for col in value_cols:
            plt.plot(data[date_col], data[col], label=col)
        plt.title("Time Series Analysis")
        plt.legend()
        os.makedirs('reports/figures', exist_ok=True)
        plt.savefig('reports/figures/time_series.png')
        plt.close()
