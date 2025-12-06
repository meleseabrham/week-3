# 🏥 AlphaCare Insurance Solutions - Risk Analytics

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![CI](https://github.com/meleseabrham/week-3/actions/workflows/ci.yml/badge.svg)](https://github.com/meleseabrham/week-3/actions)
[![DVC](https://img.shields.io/badge/DVC-Data%20Version%20Control-purple.svg)](https://dvc.org)

> Analyzing historical insurance claim data to optimize marketing strategies and identify low-risk customer segments.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Dataset](#-dataset)
- [EDA Insights](#-eda-insights)
- [Data Version Control (DVC)](#-data-version-control-dvc)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Contributing](#-contributing)

---

## 🎯 Overview

This project is part of **AlphaCare Insurance Solutions (ACIS)** analytics initiative to:

- **Optimize Marketing Strategies**: Target the right customer segments
- **Identify Low-Risk Profiles**: Discover profitable customer characteristics  
- **Build Predictive Models**: Forecast insurance charges and claims

---

## ✨ Features

### Task 1: Exploratory Data Analysis (EDA)
- ✅ Data quality assessment and cleaning
- ✅ Statistical summary and distributions
- ✅ Loss ratio analysis by categories
- ✅ Outlier detection with boxplots
- ✅ Correlation analysis
- ✅ Time series trends visualization

### Task 2: Data Version Control (DVC)
- ✅ Version-controlled data pipeline
- ✅ Local storage remote configuration
- ✅ Reproducible data workflows

---

## 🏗 Architecture

This project follows **Clean Architecture** principles for maintainability and testability:

```
┌─────────────────────────────────────────────────────────────────┐
│                        INTERFACES                               │
│                    (CLI, Notebooks)                             │
├─────────────────────────────────────────────────────────────────┤
│                       APPLICATION                               │
│               (EDAService, Interfaces)                          │
├─────────────────────────────────────────────────────────────────┤
│                         DOMAIN                                  │
│              (Entities, Business Rules)                         │
├─────────────────────────────────────────────────────────────────┤
│                     INFRASTRUCTURE                              │
│              (CSVLoader, MatplotlibPlotter)                     │
└─────────────────────────────────────────────────────────────────┘
```

| Layer | Responsibility |
|-------|----------------|
| **Domain** | Business entities (Policy, Client, Claim) and rules |
| **Application** | Use cases and abstract interfaces |
| **Infrastructure** | Data loading and visualization implementations |
| **Interfaces** | CLI entry point |

---

## 🚀 Installation

### Prerequisites
- Python 3.10+
- Git
- DVC (optional, for data versioning)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/meleseabrham/week-3.git
cd week-3

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Pull data from DVC
dvc pull
```

---

## 💻 Usage

### Run EDA Analysis

```bash
# Using CLI
python src/interfaces/cli.py --file data/insurance.csv

# Output: Generates figures in reports/figures/
```

### Run Tests

```bash
pytest tests/
```

---

## 📊 Dataset

**File**: `data/insurance.csv` (1,338 records)

| Column | Type | Description |
|--------|------|-------------|
| `age` | Numeric | Age of insured person |
| `sex` | Categorical | Gender (male/female) |
| `bmi` | Numeric | Body Mass Index |
| `children` | Numeric | Number of dependents |
| `smoker` | Categorical | Smoking status (yes/no) |
| `region` | Categorical | US geographic region |
| `charges` | Numeric | Insurance charges ($) |

---

## 📈 EDA Insights

### Key Findings

| Metric | Value |
|--------|-------|
| Mean Charges | $13,270 |
| Median Charges | $9,382 |
| Smoker Rate | ~20% |
| Highest Impact Factor | Smoking Status |

### Visualizations Generated

| Figure | Description |
|--------|-------------|
| `dist_charges.png` | Charge distribution (right-skewed) |
| `box_charges.png` | Outlier detection |
| `box_charges_by_smoker.png` | Smoker vs Non-smoker comparison |
| `bar_charges_by_region.png` | Regional charge differences |
| `scatter_age_charges.png` | Age vs Charges relationship |
| `scatter_bmi_charges.png` | BMI vs Charges relationship |

> 💡 **Key Insight**: Smokers pay ~4x higher premiums ($32K avg) compared to non-smokers ($8.4K avg)

---

## 📦 Data Version Control (DVC)

### Setup

```bash
# Initialize DVC (already done)
dvc init

# Track data files
dvc add data/insurance.csv

# Push to remote storage
dvc push
```

### Configuration

```yaml
# .dvc/config
[core]
    remote = localstorage
['remote "localstorage"']
    url = ../dvc_storage
```

### Commands

| Command | Description |
|---------|-------------|
| `dvc status` | Check data status |
| `dvc pull` | Download data from remote |
| `dvc push` | Upload data to remote |
| `dvc diff` | Show changes in data |

---

## 📁 Project Structure

```
Week 3/
├── .dvc/                    # DVC configuration
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD
├── data/
│   └── insurance.csv        # Dataset (DVC tracked)
├── reports/
│   ├── figures/             # Generated visualizations
│   └── interim_report.md    # Analysis report
├── src/
│   ├── application/
│   │   ├── eda_service.py   # EDA use case
│   │   └── interfaces.py    # Abstract interfaces
│   ├── domain/
│   │   ├── entities.py      # Business entities
│   │   └── rules.py         # Business rules
│   ├── infrastructure/
│   │   ├── csv_loader.py    # Data loading
│   │   └── plotting.py      # Visualization
│   └── interfaces/
│       └── cli.py           # CLI entry point
├── tests/
│   └── test_eda.py          # Unit tests
├── .gitignore
├── .dvcignore
├── requirements.txt
└── README.md
```

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_eda.py -v
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

## 📄 License

This project is for educational purposes as part of the 10 Academy AI Mastery program.

---

**Author**: [meleseabrham](https://github.com/meleseabrham)  
**Repository**: [week-3](https://github.com/meleseabrham/week-3)
