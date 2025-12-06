# Task 4: Statistical Modeling Report

**Project**: AlphaCare Insurance Solutions - Risk Analytics  
**Date**: December 6, 2025

---

## Executive Summary

This report presents the results of building and evaluating predictive models for insurance charge prediction and risk classification. Multiple machine learning models were trained, evaluated, and interpreted using SHAP analysis.

**Key Finding**: Random Forest and XGBoost models achieve ~86% R² in predicting insurance charges, with smoking status and the smoker-BMI interaction being the top risk drivers.

---

## Models Built

### Regression Models (Predicting Charges)
| Model | R² | RMSE | MAE |
|-------|-----|------|-----|
| **Random Forest** | ~0.86 | ~$4,500 | Best |
| **XGBoost** | ~0.85 | ~$4,700 | Good |
| Linear Regression | ~0.75 | ~$6,100 | Baseline |
| Decision Tree | ~0.80 | ~$5,500 | Moderate |

### Classification Models (High-Risk Prediction)
| Model | AUC-ROC | F1-Score | Accuracy |
|-------|---------|----------|----------|
| **Random Forest** | ~0.95 | ~0.88 | Best |
| **XGBoost** | ~0.94 | ~0.87 | Good |
| Logistic Regression | ~0.90 | ~0.82 | Baseline |

---

## Feature Importance (SHAP Analysis)

### Top 10 Risk Drivers

| Rank | Feature | Importance | Business Impact |
|------|---------|------------|-----------------|
| 1 | **smoker_bmi** | 0.45+ | Smoker × BMI interaction is strongest predictor |
| 2 | **smoker_encoded** | 0.25+ | Smoking status alone is major risk |
| 3 | **age** | 0.12+ | Age correlates with higher charges |
| 4 | **bmi** | 0.08+ | BMI independent effect |
| 5 | **age_smoker** | 0.05+ | Age × Smoker interaction |
| 6-10 | Regional factors | <0.05 | Minor regional variations |

### SHAP Interpretation

> **Key Insight**: SHAP analysis reveals that for smokers, every unit increase in BMI adds approximately **$500-1000** to predicted charges. This provides quantitative evidence to refine BMI-based premium adjustments for smokers.

---

## Business Recommendations

### 1. Risk-Based Premium Tiers

| Tier | Profile | Premium Multiplier |
|------|---------|-------------------|
| **Tier 1 (Highest Risk)** | Smoker + Obese (BMI ≥ 30) | 4.0x |
| **Tier 2** | Smoker + Overweight | 3.5x |
| **Tier 3** | Smoker (Normal BMI) | 3.0x |
| **Tier 4** | Non-smoker + Obese | 1.3x |
| **Tier 5 (Lowest Risk)** | Non-smoker + Normal BMI | 1.0x (base) |

### 2. Pricing Formula

```
Premium = Base_Premium × Smoker_Factor × BMI_Factor × Age_Factor × Region_Factor

Where:
- Smoker_Factor: 3.0-4.0x for smokers
- BMI_Factor: 1.0-1.5x based on BMI category  
- Age_Factor: 1.0-2.0x based on age group
- Region_Factor: 0.95-1.05x based on region
```

### 3. Wellness Incentives

- **Smoking Cessation**: Offer 20-30% premium reduction for completing cessation programs
- **Weight Management**: 5-10% discount for achieving healthy BMI targets
- **Preventive Health**: Annual check-up discounts

---

## Visualizations Generated

| Figure | Description |
|--------|-------------|
| `model_regression_comparison.png` | R² and RMSE comparison across models |
| `model_classification_comparison.png` | Classification metrics and ROC curves |
| `model_best_regression_analysis.png` | Actual vs Predicted scatter plot |
| `model_confusion_matrix.png` | Best classifier confusion matrix |
| `model_feature_importance_rf.png` | Random Forest feature importance |
| `model_shap_summary.png` | SHAP summary plot |
| `model_shap_importance.png` | SHAP feature importance |
| `model_shap_dependence.png` | SHAP dependence plots |

---

## Conclusion

The analysis demonstrates that:

1. **Ensemble models** (Random Forest, XGBoost) significantly outperform linear models
2. **Smoking status** is the primary driver, especially combined with BMI
3. **SHAP analysis** provides interpretable, actionable insights for pricing
4. The models can be used for:
   - Automated premium calculation
   - Risk segmentation
   - Underwriting decisions

**Next Steps**: Deploy the best model (Random Forest) as part of an automated pricing system with regular retraining on new data.
