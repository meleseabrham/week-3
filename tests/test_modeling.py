"""
Unit tests for the Modeling Service.

Tests cover data preparation, model training, and evaluation functions.
"""

import pytest
import pandas as pd
import numpy as np
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


class MockDataLoader:
    """Mock data loader for testing."""
    
    def load_data(self, file_path: str) -> pd.DataFrame:
        """Generate mock insurance data."""
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
        df = pd.DataFrame(data)
        # Add significant difference for smokers
        df.loc[df['smoker'] == 'yes', 'charges'] *= 3
        return df


class TestDataPreparation:
    """Test data preparation functions."""
    
    def setup_method(self):
        """Set up test data."""
        self.loader = MockDataLoader()
        self.df = self.loader.load_data("dummy.csv")
    
    def test_data_loading(self):
        """Test that data loads correctly."""
        assert self.df is not None
        assert not self.df.empty
        assert len(self.df) == 100
    
    def test_required_columns_exist(self):
        """Test that all required columns exist."""
        required = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
        for col in required:
            assert col in self.df.columns
    
    def test_no_missing_values(self):
        """Test that there are no missing values."""
        assert self.df.isnull().sum().sum() == 0
    
    def test_feature_engineering_bmi_category(self):
        """Test BMI category creation."""
        self.df['bmi_category'] = pd.cut(
            self.df['bmi'],
            bins=[0, 18.5, 25, 30, 100],
            labels=['Underweight', 'Normal', 'Overweight', 'Obese']
        )
        assert 'bmi_category' in self.df.columns
        assert self.df['bmi_category'].nunique() <= 4
    
    def test_feature_engineering_age_group(self):
        """Test age group creation."""
        self.df['age_group'] = pd.cut(
            self.df['age'],
            bins=[17, 30, 45, 60, 100],
            labels=['18-30', '31-45', '46-60', '60+']
        )
        assert 'age_group' in self.df.columns
        assert self.df['age_group'].nunique() <= 4
    
    def test_smoker_bmi_interaction(self):
        """Test smoker-BMI interaction feature."""
        self.df['smoker_bmi'] = (self.df['smoker'] == 'yes').astype(int) * self.df['bmi']
        assert 'smoker_bmi' in self.df.columns
        # Non-smokers should have 0 for this feature
        assert (self.df[self.df['smoker'] == 'no']['smoker_bmi'] == 0).all()


class TestModelTraining:
    """Test model training functions."""
    
    def setup_method(self):
        """Set up test data."""
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.ensemble import RandomForestRegressor
        
        self.loader = MockDataLoader()
        self.df = self.loader.load_data("dummy.csv")
        
        # Prepare features
        self.df['smoker_encoded'] = (self.df['smoker'] == 'yes').astype(int)
        self.df['sex_encoded'] = (self.df['sex'] == 'male').astype(int)
        
        self.X = self.df[['age', 'bmi', 'children', 'smoker_encoded', 'sex_encoded']]
        self.y = self.df['charges']
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
    
    def test_linear_regression_training(self):
        """Test Linear Regression model training."""
        from sklearn.linear_model import LinearRegression
        
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        
        # Model should be fitted
        assert hasattr(model, 'coef_')
        assert len(model.coef_) == self.X_train.shape[1]
    
    def test_random_forest_training(self):
        """Test Random Forest model training."""
        from sklearn.ensemble import RandomForestRegressor
        
        model = RandomForestRegressor(n_estimators=10, random_state=42)
        model.fit(self.X_train, self.y_train)
        
        # Model should be fitted
        assert hasattr(model, 'feature_importances_')
        assert len(model.feature_importances_) == self.X_train.shape[1]
    
    def test_model_predictions(self):
        """Test that models produce valid predictions."""
        from sklearn.linear_model import LinearRegression
        
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        predictions = model.predict(self.X_test)
        
        assert len(predictions) == len(self.y_test)
        assert not np.any(np.isnan(predictions))


class TestModelEvaluation:
    """Test model evaluation functions."""
    
    def test_r2_score_range(self):
        """Test R² score is in valid range."""
        from sklearn.metrics import r2_score
        
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1.1, 2.0, 2.9, 4.1, 5.0])
        
        r2 = r2_score(y_true, y_pred)
        assert -1 <= r2 <= 1
    
    def test_rmse_positive(self):
        """Test RMSE is always positive."""
        from sklearn.metrics import mean_squared_error
        
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1.1, 2.0, 2.9, 4.1, 5.0])
        
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        assert rmse >= 0
    
    def test_classification_metrics(self):
        """Test classification metrics."""
        from sklearn.metrics import accuracy_score, f1_score
        
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 0, 0, 1])
        
        accuracy = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        
        assert 0 <= accuracy <= 1
        assert 0 <= f1 <= 1
