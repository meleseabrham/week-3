import pytest
import pandas as pd
import numpy as np
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.application.ab_testing_service import ABTestingService
from src.infrastructure.csv_loader import CSVLoader


class MockLoader(CSVLoader):
    """Mock loader with known data for testing."""
    def load_data(self, file_path: str) -> pd.DataFrame:
        np.random.seed(42)
        n = 100
        data = {
            'age': np.random.randint(18, 65, n),
            'sex': np.random.choice(['male', 'female'], n),
            'bmi': np.random.uniform(18, 40, n),
            'children': np.random.randint(0, 5, n),
            'smoker': np.random.choice(['yes', 'no'], n, p=[0.2, 0.8]),
            'region': np.random.choice(['northeast', 'northwest', 'southeast', 'southwest'], n),
            'charges': np.random.uniform(1000, 50000, n)
        }
        # Add significant difference for smokers
        df = pd.DataFrame(data)
        df.loc[df['smoker'] == 'yes', 'charges'] *= 3
        return df


class TestABTestingService:
    """Test suite for ABTestingService."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.loader = MockLoader()
        self.service = ABTestingService(self.loader)
    
    def test_service_initialization(self):
        """Test service initializes correctly."""
        assert self.service is not None
        assert self.service.alpha == 0.05
    
    def test_load_and_prepare_data(self):
        """Test data loading and BMI category creation."""
        df = self.service.load_and_prepare_data("dummy.csv")
        
        assert df is not None
        assert not df.empty
        assert 'bmi_category' in df.columns
        assert df['bmi_category'].dropna().nunique() <= 4
    
    def test_regional_differences(self):
        """Test regional hypothesis testing."""
        df = self.service.load_and_prepare_data("dummy.csv")
        result = self.service.test_regional_differences(df)
        
        assert 'hypothesis' in result
        assert 'test' in result
        assert 'f_statistic' in result
        assert 'p_value' in result
        assert 'reject_null' in result
        assert 'interpretation' in result
        assert result['test'] == 'One-way ANOVA'
    
    def test_gender_differences(self):
        """Test gender hypothesis testing."""
        df = self.service.load_and_prepare_data("dummy.csv")
        result = self.service.test_gender_differences(df)
        
        assert 'hypothesis' in result
        assert 'test' in result
        assert 't_statistic' in result
        assert 'p_value' in result
        assert 'cohens_d' in result
        assert 'male_mean' in result
        assert 'female_mean' in result
        assert result['test'] == 'Independent t-test'
    
    def test_smoker_differences(self):
        """Test smoker hypothesis testing."""
        df = self.service.load_and_prepare_data("dummy.csv")
        result = self.service.test_smoker_differences(df)
        
        assert 'hypothesis' in result
        assert 'p_value' in result
        assert 'smoker_mean' in result
        assert 'non_smoker_mean' in result
        # With our mock data, smokers should have higher charges
        assert result['smoker_mean'] > result['non_smoker_mean']
    
    def test_bmi_category_differences(self):
        """Test BMI category hypothesis testing."""
        df = self.service.load_and_prepare_data("dummy.csv")
        result = self.service.test_bmi_category_differences(df)
        
        assert 'hypothesis' in result
        assert 'test' in result
        assert 'f_statistic' in result
        assert 'p_value' in result
        assert result['test'] == 'One-way ANOVA'
    
    def test_run_all_tests(self):
        """Test running all hypothesis tests."""
        results = self.service.run_all_tests("dummy.csv")
        
        assert 'regional' in results
        assert 'gender' in results
        assert 'smoker' in results
        assert 'bmi' in results
        
        # All results should have p-values
        for key, result in results.items():
            assert 'p_value' in result
            assert 0 <= result['p_value'] <= 1
    
    def test_reject_null_is_boolean(self):
        """Test that reject_null is always boolean type."""
        results = self.service.run_all_tests("dummy.csv")
        
        for key, result in results.items():
            assert isinstance(result['reject_null'], (bool, np.bool_))
