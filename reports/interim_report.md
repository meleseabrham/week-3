# Interim Report: Task 1 & Task 2

**Project**: AlphaCare Insurance Solutions - Risk Analytics  
**Date**: December 5, 2024  
**Repository**: [https://github.com/meleseabrham/week-3](https://github.com/meleseabrham/week-3)

---

## Executive Summary

This report summarizes the work completed in Task 1 (EDA & Project Setup) and Task 2 (Data Version Control). The project uses Clean Architecture and is fully version-controlled with Git and DVC.

---

## Task 1: Project Setup & EDA

### 1.1 Git & GitHub Setup
- Initialized Git repository with proper `.gitignore` and `README.md`.
- Set up CI/CD pipeline using GitHub Actions (`.github/workflows/ci.yml`).
- Created `task-1` branch for development.

### 1.2 Exploratory Data Analysis (EDA)

#### Key Findings

| Metric | Value |
|--------|-------|
| **Overall Loss Ratio** | 39.29% |
| **Highest Risk Province** | Limpopo (107.14%) |
| **Lowest Risk Province** | Eastern Cape (0%) |
| **Female Loss Ratio** | 49.5% |
| **Male Loss Ratio** | 30.9% |

#### Visualizations Generated
- Distribution plots for `TotalPremium` and `TotalClaims`.
- Bar charts for Loss Ratio by Province, VehicleType, and Gender.
- Time series plot for temporal trends.
- Box plots for outlier detection.

All plots are saved in `reports/figures/`.

---

## Task 2: Data Version Control (DVC)

### 2.1 Setup
- Installed and initialized DVC.
- Configured local remote storage (`dvc_storage/`).

### 2.2 Data Tracking
- Tracked `data/insurance_claims.csv` with DVC.
- Ensured `.csv` and `.dvc` files are excluded from GitHub via `.gitignore`.

### 2.3 Repository Structure
```
Week 3/
├── .dvc/                 # DVC config
├── .github/workflows/    # CI/CD
├── data/                 # Tracked by DVC (only .gitkeep on GitHub)
├── reports/figures/      # Generated plots
├── src/                  # Clean Architecture source code
│   ├── application/      # Use cases & interfaces
│   ├── domain/           # Business entities & rules
│   ├── infrastructure/   # Data loaders & plotting
│   └── interfaces/       # CLI entry point
├── tests/                # Unit tests
└── requirements.txt      # Dependencies
```

---

## Branches Merged to Main
- `task-1`: Project setup, EDA implementation, CI/CD.
- `task-2`: DVC setup, data tracking.

---

## Next Steps
- **Task 3**: A/B Hypothesis Testing (Risk differences by province, gender, etc.)
- **Task 4**: Predictive Modeling (Premium prediction using ML)
