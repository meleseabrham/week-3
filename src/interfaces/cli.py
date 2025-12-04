import argparse
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.infrastructure.csv_loader import CSVLoader
from src.infrastructure.plotting import MatplotlibPlotter
from src.application.eda_service import EDAService

def main():
    parser = argparse.ArgumentParser(description="Insurance Risk Analytics EDA")
    parser.add_argument("--file", type=str, help="Path to the dataset CSV file")
    args = parser.parse_args()

    if args.file:
        loader = CSVLoader()
        plotter = MatplotlibPlotter()
        service = EDAService(loader, plotter)
        service.perform_initial_analysis(args.file)
    else:
        print("Please provide a file path using --file")

if __name__ == "__main__":
    main()
