from src.application.interfaces import IDataLoader
import pandas as pd
from scipy import stats
from typing import Dict, Tuple, Any

class ABTestingService:
    """Service for A/B Hypothesis Testing on insurance data."""
    
    def __init__(self, data_loader: IDataLoader):
        self.data_loader = data_loader
        self.alpha = 0.05  # Significance level
        
    def load_and_prepare_data(self, file_path: str) -> pd.DataFrame:
        """Load data and add BMI categories."""
        df = self.data_loader.load_data(file_path)
        
        # Create BMI categories for segmentation
        df['bmi_category'] = pd.cut(
            df['bmi'], 
            bins=[0, 18.5, 25, 30, 100],
            labels=['Underweight', 'Normal', 'Overweight', 'Obese']
        )
        return df
    
    def test_regional_differences(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        H₀: No significant difference in charges across regions.
        Test: One-way ANOVA
        """
        regions = df['region'].unique()
        groups = [df[df['region'] == r]['charges'].values for r in regions]
        
        # Perform ANOVA
        f_stat, p_value = stats.f_oneway(*groups)
        
        # Calculate group statistics
        group_stats = df.groupby('region')['charges'].agg(['mean', 'std', 'count'])
        
        return {
            'hypothesis': 'H₀: No significant difference in charges across regions',
            'test': 'One-way ANOVA',
            'f_statistic': f_stat,
            'p_value': p_value,
            'reject_null': p_value < self.alpha,
            'group_statistics': group_stats.to_dict(),
            'interpretation': self._interpret_result(p_value, 'regional')
        }
    
    def test_gender_differences(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        H₀: No significant risk difference between Women and Men.
        Test: Independent t-test
        """
        male_charges = df[df['sex'] == 'male']['charges']
        female_charges = df[df['sex'] == 'female']['charges']
        
        # Perform t-test
        t_stat, p_value = stats.ttest_ind(male_charges, female_charges)
        
        # Effect size (Cohen's d)
        pooled_std = ((male_charges.std()**2 + female_charges.std()**2) / 2) ** 0.5
        cohens_d = (male_charges.mean() - female_charges.mean()) / pooled_std
        
        return {
            'hypothesis': 'H₀: No significant risk difference between Women and Men',
            'test': 'Independent t-test',
            't_statistic': t_stat,
            'p_value': p_value,
            'cohens_d': cohens_d,
            'reject_null': p_value < self.alpha,
            'male_mean': male_charges.mean(),
            'female_mean': female_charges.mean(),
            'interpretation': self._interpret_result(p_value, 'gender')
        }
    
    def test_smoker_differences(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        H₀: No significant risk difference between Smokers and Non-smokers.
        Test: Independent t-test
        """
        smoker_charges = df[df['smoker'] == 'yes']['charges']
        non_smoker_charges = df[df['smoker'] == 'no']['charges']
        
        # Perform t-test
        t_stat, p_value = stats.ttest_ind(smoker_charges, non_smoker_charges)
        
        # Effect size (Cohen's d)
        pooled_std = ((smoker_charges.std()**2 + non_smoker_charges.std()**2) / 2) ** 0.5
        cohens_d = (smoker_charges.mean() - non_smoker_charges.mean()) / pooled_std
        
        return {
            'hypothesis': 'H₀: No significant risk difference between Smokers and Non-smokers',
            'test': 'Independent t-test',
            't_statistic': t_stat,
            'p_value': p_value,
            'cohens_d': cohens_d,
            'reject_null': p_value < self.alpha,
            'smoker_mean': smoker_charges.mean(),
            'non_smoker_mean': non_smoker_charges.mean(),
            'interpretation': self._interpret_result(p_value, 'smoker')
        }
    
    def test_bmi_category_differences(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        H₀: No significant difference in charges across BMI categories.
        Test: One-way ANOVA
        """
        categories = df['bmi_category'].dropna().unique()
        groups = [df[df['bmi_category'] == c]['charges'].values for c in categories]
        
        # Perform ANOVA
        f_stat, p_value = stats.f_oneway(*groups)
        
        # Calculate group statistics
        group_stats = df.groupby('bmi_category')['charges'].agg(['mean', 'std', 'count'])
        
        return {
            'hypothesis': 'H₀: No significant difference in charges across BMI categories',
            'test': 'One-way ANOVA',
            'f_statistic': f_stat,
            'p_value': p_value,
            'reject_null': p_value < self.alpha,
            'group_statistics': group_stats.to_dict(),
            'interpretation': self._interpret_result(p_value, 'bmi')
        }
    
    def run_all_tests(self, file_path: str) -> Dict[str, Dict]:
        """Run all hypothesis tests and return results."""
        df = self.load_and_prepare_data(file_path)
        
        return {
            'regional': self.test_regional_differences(df),
            'gender': self.test_gender_differences(df),
            'smoker': self.test_smoker_differences(df),
            'bmi': self.test_bmi_category_differences(df)
        }
    
    def _interpret_result(self, p_value: float, test_type: str) -> str:
        """Generate business interpretation of the result."""
        if p_value < self.alpha:
            interpretations = {
                'regional': f"We REJECT the null hypothesis (p={p_value:.4f}). There are significant differences in insurance charges across regions. Consider regional premium adjustments.",
                'gender': f"We REJECT the null hypothesis (p={p_value:.4f}). There are significant differences in insurance charges between genders. Review gender-based risk assessment policies.",
                'smoker': f"We REJECT the null hypothesis (p={p_value:.4f}). Smokers have significantly different insurance charges than non-smokers. Smoking status is a major risk factor for premium calculation.",
                'bmi': f"We REJECT the null hypothesis (p={p_value:.4f}). BMI categories show significant differences in insurance charges. Consider BMI-based risk segmentation."
            }
        else:
            interpretations = {
                'regional': f"We FAIL TO REJECT the null hypothesis (p={p_value:.4f}). No significant regional differences in charges. Uniform regional pricing may be appropriate.",
                'gender': f"We FAIL TO REJECT the null hypothesis (p={p_value:.4f}). No significant gender-based differences in charges. Gender-neutral pricing is supported.",
                'smoker': f"We FAIL TO REJECT the null hypothesis (p={p_value:.4f}). No significant difference between smokers and non-smokers. This is unexpected and warrants investigation.",
                'bmi': f"We FAIL TO REJECT the null hypothesis (p={p_value:.4f}). No significant differences across BMI categories. BMI may not be a primary risk driver."
            }
        return interpretations.get(test_type, "Interpretation not available.")
