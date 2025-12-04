# AlphaCare Insurance Solutions - Risk Analytics

## Overview
This project focuses on analyzing historical insurance claim data to optimize marketing strategies and identify low-risk targets for AlphaCare Insurance Solutions (ACIS).

## Objectives
- **Exploratory Data Analysis (EDA)**: Understand risk and profitability patterns.
- **Hypothesis Testing**: Validate assumptions about risk across provinces, zip codes, and demographics.
- **Predictive Modeling**: Build models to predict total claims and optimal premiums.

## Architecture
This project follows **Clean Architecture** principles:
- **Domain**: Business entities and rules.
- **Application**: Use cases and interfaces.
- **Infrastructure**: External implementations (Data loading, Plotting).
- **Interfaces**: Entry points (CLI, Notebooks).

## Setup
1. Clone the repository.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run analysis: `python src/interfaces/cli.py`
