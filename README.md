# 🏥 AlphaCare Insurance Solutions - Risk Analytics

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![CI](https://github.com/meleseabrham/week-3/actions/workflows/ci.yml/badge.svg)](https://github.com/meleseabrham/week-3/actions)
[![DVC](https://img.shields.io/badge/DVC-Data%20Version%20Control-purple.svg)](https://dvc.org)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)

> A comprehensive insurance risk analytics project featuring EDA, hypothesis testing, and machine learning models for risk-based pricing optimization.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Results](#-key-results)
- [Project Tasks](#-project-tasks)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Dataset](#-dataset)
- [Notebooks](#-notebooks)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)

---

## 🎯 Overview

This project analyzes historical insurance data for **AlphaCare Insurance Solutions (ACIS)** to:

- 📊 **Understand Risk Patterns**: Identify key factors driving insurance charges
- 🧪 **Validate Hypotheses**: Statistically test risk differences across segments
- 🤖 **Build Predictive Models**: Develop ML models for charge prediction
- 💰 **Optimize Pricing**: Create data-driven premium recommendations

---

## 🏆 Key Results

### Risk Drivers Identified
| Rank | Factor | Impact |
|------|--------|--------|
| 1 | **Smoking Status** | 3.8x higher charges |
| 2 | **BMI (Obese)** | 30-50% higher charges |
| 3 | **Age** | Linear increase with age |
| 4 | **Region** | Minor variations |

### Model Performance
| Model | R² Score | Use Case |
|-------|----------|----------|
| Random Forest | **86%** | Charge Prediction |
| XGBoost | 85% | Risk Classification |
| Linear Regression | 75% | Baseline |

### Business Impact
- ✅ Automated risk scoring for new policies
- ✅ Data-driven premium tier recommendations
- ✅ Identified high-risk segments for targeted interventions

---

## 📌 Project Tasks

### ✅ Task 1: Project Setup & EDA
- Git repository with CI/CD pipeline
- Clean Architecture implementation
- Comprehensive exploratory data analysis
- 11 EDA visualizations

### ✅ Task 2: Data Version Control (DVC)
- DVC initialization and configuration
- Local remote storage setup
- Data tracking with `.gitignore`

### ✅ Task 3: A/B Hypothesis Testing
- 4 statistical hypotheses tested
- Chi-squared and t-tests/ANOVA
- Business recommendations

| Hypothesis | Result |
|------------|--------|
| Regional differences | Not significant |
| Gender differences | Not significant |
| Smoker differences | **REJECT H₀** ✅ |
| BMI differences | **REJECT H₀** ✅ |

### ✅ Task 4: Statistical Modeling
- 4 regression models + 4 classification models
- SHAP interpretability analysis
- Risk-based pricing framework

---

## 🏗 Architecture

This project follows **Clean Architecture** principles:

```
┌─────────────────────────────────────────────────────────────────┐
│                        INTERFACES                               │
│                    (CLI, Notebooks)                             │
├─────────────────────────────────────────────────────────────────┤
│                       APPLICATION                               │
│         (EDAService, ABTestingService, ModelingService)         │
├─────────────────────────────────────────────────────────────────┤
│                         DOMAIN                                  │
│              (Entities, Business Rules)                         │
├─────────────────────────────────────────────────────────────────┤
│                     INFRASTRUCTURE                              │
│              (CSVLoader, MatplotlibPlotter)                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10+
- Git
- pip

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/meleseabrham/week-3.git
cd week-3

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Pull data from DVC
dvc pull
```

### Dependencies
```
pandas, numpy, matplotlib, seaborn, scipy, scikit-learn, pytest, dvc, xgboost, shap
```

---

## 💻 Usage

### Run EDA Analysis
```bash
python src/interfaces/cli.py --file data/insurance.csv
```

### Run Jupyter Notebooks
```bash
jupyter notebook notebooks/
```

### Run Tests
```bash
pytest tests/ -v
```

---

## 📊 Dataset

**File**: `data/insurance.csv` (1,338 records)

| Column | Type | Description |
|--------|------|-------------|
| `age` | Numeric | Age of insured (18-64) |
| `sex` | Categorical | Gender (male/female) |
| `bmi` | Numeric | Body Mass Index |
| `children` | Numeric | Number of dependents |
| `smoker` | Categorical | Smoking status (yes/no) |
| `region` | Categorical | US region (4 regions) |
| `charges` | Numeric | Insurance charges ($) |

### Key Statistics
| Metric | Value |
|--------|-------|
| Mean Charges | $13,270 |
| Median Charges | $9,382 |
| Smoker Premium | ~$32,000 |
| Non-Smoker Premium | ~$8,400 |

---

## 📓 Notebooks

| Notebook | Task | Description |
|----------|------|-------------|
| `eda_analysis.ipynb` | Task 1-2 | Exploratory Data Analysis |
| `ab_testing.ipynb` | Task 3 | Hypothesis Testing |
| `modeling.ipynb` | Task 4 | ML Models & SHAP |

### Visualizations Generated
- **EDA**: 11 figures (distributions, correlations, dashboards)
- **Hypothesis Testing**: 6 figures (comparisons, heatmaps)
- **Modeling**: 5 figures (ROC curves, SHAP plots)

---

## 📁 Project Structure

```
Week 3/
├── .dvc/                         # DVC configuration
├── .github/
│   └── workflows/ci.yml          # CI/CD pipeline
├── data/
│   └── insurance.csv             # Dataset
├── notebooks/
│   ├── eda_analysis.ipynb        # Task 1-2: EDA
│   ├── ab_testing.ipynb          # Task 3: Hypothesis Testing
│   └── modeling.ipynb            # Task 4: ML Modeling
├── reports/
│   ├── figures/                  # 29 visualizations
│   ├── interim_report.md         # Task 1-2 report
│   ├── hypothesis_report.md      # Task 3 report
│   └── modeling_report.md        # Task 4 report
├── src/
│   ├── application/
│   │   ├── eda_service.py        # EDA use case
│   │   ├── ab_testing_service.py # Hypothesis testing
│   │   └── interfaces.py         # Abstract interfaces
│   ├── domain/
│   │   ├── entities.py           # Business entities
│   │   └── rules.py              # Business rules
│   ├── infrastructure/
│   │   ├── csv_loader.py         # Data loading
│   │   └── plotting.py           # Visualization
│   └── interfaces/
│       └── cli.py                # CLI entry point
├── tests/
│   ├── test_eda.py               # EDA tests
│   └── test_ab_testing.py        # Hypothesis tests
├── .gitignore
├── .dvcignore
├── requirements.txt
└── README.md
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_ab_testing.py -v
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "feat: add your feature"`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

### Commit Convention
| Prefix | Description |
|--------|-------------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation |
| `test:` | Tests |
| `chore:` | Maintenance |

---

## � Reports

| Report | Description |
|--------|-------------|
| [Interim Report](reports/interim_report.md) | Task 1-2 summary |
| [Hypothesis Report](reports/hypothesis_report.md) | A/B testing results |
| [Modeling Report](reports/modeling_report.md) | ML model comparison |

---

## 🔗 Links

- **Repository**: [github.com/meleseabrham/week-3](https://github.com/meleseabrham/week-3)
- **Author**: [@meleseabrham](https://github.com/meleseabrham)
- **Program**: 10 Academy AI Mastery

---

## 📄 License

This project is for educational purposes as part of the 10 Academy AI Mastery program.

---

<p align="center">
  Made with ❤️ for AlphaCare Insurance Solutions
</p>
