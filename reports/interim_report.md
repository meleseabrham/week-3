# Interim Report: Task 1 & Task 2

**Project**: AlphaCare Insurance Solutions - Risk Analytics  
**Date**: December 5, 2025  
**Repository**: [https://github.com/meleseabrham/week-3](https://github.com/meleseabrham/week-3)

---

## Executive Summary

This report summarizes the work completed in Task 1 (EDA & Project Setup) and Task 2 (Data Version Control). The project analyzes insurance data to identify risk patterns and optimize marketing strategies. The codebase follows Clean Architecture principles and is fully version-controlled with Git and DVC.

---

## Task 1: Project Setup & EDA

### 1.1 Git & GitHub Setup
- ✅ Initialized Git repository with proper `.gitignore` and `README.md`
- ✅ Set up CI/CD pipeline using GitHub Actions (`.github/workflows/ci.yml`)
- ✅ Created development branches (`task-1`, `task-2`)
- ✅ Regular commits with descriptive messages

### 1.2 Data Overview

**Dataset**: `insurance.csv` (1,338 records, 7 features)

| Column | Type | Description |
|--------|------|-------------|
| `age` | Numeric | Age of the insured person |
| `sex` | Categorical | Gender (male/female) |
| `bmi` | Numeric | Body Mass Index |
| `children` | Numeric | Number of dependents |
| `smoker` | Categorical | Smoking status (yes/no) |
| `region` | Categorical | Geographic region (northeast, northwest, southeast, southwest) |
| `charges` | Numeric | Insurance charges/premiums |

### 1.3 Exploratory Data Analysis (EDA)

#### Key Statistical Findings

| Metric | Value |
|--------|-------|
| **Total Records** | 1,338 |
| **Mean Charges** | $13,270 |
| **Median Charges** | $9,382 |
| **Min Charges** | $1,122 |
| **Max Charges** | $63,770 |
| **Smokers** | ~20% of dataset |

#### Key Insights

1. **Smoking Status**: Smokers have significantly higher insurance charges (avg ~$32,000) compared to non-smokers (avg ~$8,400)
2. **Age Impact**: Strong positive correlation between age and insurance charges
3. **BMI Effect**: Higher BMI correlates with increased charges, especially for smokers
4. **Regional Variation**: Southeast region shows slightly higher average charges
5. **Outliers**: High-value claims primarily from older smokers with high BMI

### 1.4 Visualizations Generated

| Figure | Description |
|--------|-------------|
| `dist_charges.png` | Distribution of insurance charges (right-skewed) |
| `box_charges.png` | Boxplot showing charge outliers |
| `box_charges_by_smoker.png` | Charge comparison by smoking status |
| `bar_charges_by_region.png` | Average charges by geographic region |
| `scatter_age_charges.png` | Age vs Charges relationship (colored by smoker) |
| `scatter_bmi_charges.png` | BMI vs Charges relationship (colored by smoker) |

All plots are saved in `reports/figures/`.

---

## Task 2: Data Version Control (DVC)

### 2.1 Setup
- ✅ Installed DVC via `pip install dvc`
- ✅ Initialized DVC in project directory (`dvc init`)
- ✅ Configured local remote storage (`dvc_storage/`)

### 2.2 Data Tracking
- ✅ Data files tracked with DVC
- ✅ `.csv` files excluded from Git via `.gitignore`
- ✅ `.dvc` tracking files committed to repository

### 2.3 Repository Structure
```
Week 3/
├── .dvc/                 # DVC configuration
├── .github/workflows/    # CI/CD pipeline
├── data/                 # Data files (tracked by DVC)
│   └── insurance.csv     # Main dataset (1,338 records)
├── reports/
│   ├── figures/          # Generated EDA plots
│   └── interim_report.md # This report
├── src/                  # Clean Architecture source code
│   ├── application/      # Use cases & interfaces (eda_service.py)
│   ├── domain/           # Business entities & rules
│   ├── infrastructure/   # Data loaders & plotting
│   └── interfaces/       # CLI entry point
├── tests/                # Unit tests
├── integrate_data.py     # Data integration script
└── requirements.txt      # Dependencies
```

---

## Dependencies

```
pandas
numpy
matplotlib
seaborn
scipy
scikit-learn
pytest
dvc
```

---

## Next Steps

### Task 3: A/B Hypothesis Testing
- Test for significant differences in charges between regions
- Test for significant differences between smokers and non-smokers
- Test for gender-based charge differences
- Test for age group risk differences

### Task 4: Machine Learning & Statistical Modeling
- Build linear regression model to predict insurance charges
- Feature importance analysis (age, BMI, smoking status, region)
- Model evaluation and optimization

---

## Conclusion

Tasks 1 and 2 have been successfully completed. The project infrastructure is in place with:
- Version-controlled codebase on GitHub
- DVC-tracked data files
- Clean Architecture implementation
- Comprehensive EDA with visualizations

The analysis reveals that **smoking status**, **age**, and **BMI** are the primary drivers of insurance charges, providing actionable insights for risk segmentation and premium optimization.
