"""
Data Integration Script
Integrates insurance.csv into insurance_claims.csv and regenerates EDA figures.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
DATA_DIR = 'data'
FIGURES_DIR = 'reports/figures'
INSURANCE_FILE = os.path.join(DATA_DIR, 'insurance.csv')
CLAIMS_FILE = os.path.join(DATA_DIR, 'insurance_claims.csv')
OUTPUT_FILE = os.path.join(DATA_DIR, 'insurance_claims_integrated.csv')

# Ensure figures directory exists
os.makedirs(FIGURES_DIR, exist_ok=True)

def load_and_explore():
    """Load both CSV files and show their structure."""
    print("=" * 60)
    print("LOADING DATA FILES")
    print("=" * 60)
    
    # Load insurance.csv
    print(f"\n1. Loading {INSURANCE_FILE}...")
    df_insurance = pd.read_csv(INSURANCE_FILE, low_memory=False)
    print(f"   Shape: {df_insurance.shape}")
    print(f"   Columns: {list(df_insurance.columns[:10])}...")
    
    # Load insurance_claims.csv
    print(f"\n2. Loading {CLAIMS_FILE}...")
    df_claims = pd.read_csv(CLAIMS_FILE, low_memory=False)
    print(f"   Shape: {df_claims.shape}")
    print(f"   Columns: {list(df_claims.columns[:10])}...")
    
    return df_insurance, df_claims

def integrate_data(df_insurance, df_claims):
    """Integrate the two dataframes."""
    print("\n" + "=" * 60)
    print("INTEGRATING DATA")
    print("=" * 60)
    
    # Clean column names
    df_insurance.columns = df_insurance.columns.str.strip()
    df_claims.columns = df_claims.columns.str.strip()
    
    # Find common columns
    common_cols = set(df_insurance.columns) & set(df_claims.columns)
    insurance_only = set(df_insurance.columns) - set(df_claims.columns)
    claims_only = set(df_claims.columns) - set(df_insurance.columns)
    
    print(f"\nCommon columns: {len(common_cols)}")
    print(f"Columns only in insurance.csv: {len(insurance_only)}")
    print(f"Columns only in insurance_claims.csv: {len(claims_only)}")
    
    # Strategy: Concatenate both datasets (assuming similar structure)
    # If structures are very different, merge on common key columns
    
    if len(common_cols) > 5:  # If many common columns, likely same structure
        print("\nConcatenating datasets (similar structure detected)...")
        # Align columns and concatenate
        all_cols = list(set(df_insurance.columns) | set(df_claims.columns))
        df_integrated = pd.concat([df_insurance, df_claims], ignore_index=True, sort=False)
    else:  # Different structures - try to find key columns for merge
        print("\nAttempting merge on potential key columns...")
        potential_keys = ['PolicyNumber', 'Policy_Number', 'policy_number', 'id', 'ID', 'PolicyID']
        key_col = None
        for key in potential_keys:
            if key in common_cols:
                key_col = key
                break
        
        if key_col:
            print(f"   Merging on: {key_col}")
            df_integrated = pd.merge(df_claims, df_insurance, on=key_col, how='outer', suffixes=('', '_insurance'))
        else:
            print("   No key column found, concatenating with all columns...")
            df_integrated = pd.concat([df_insurance, df_claims], ignore_index=True, sort=False)
    
    print(f"\nIntegrated dataset shape: {df_integrated.shape}")
    
    # Save integrated data
    df_integrated.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved integrated data to: {OUTPUT_FILE}")
    
    return df_integrated

def generate_figures(df):
    """Generate EDA figures from the integrated data."""
    print("\n" + "=" * 60)
    print("GENERATING FIGURES")
    print("=" * 60)
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Convert numeric columns
    for col in ['TotalPremium', 'TotalClaims']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Convert date column
    if 'TransactionMonth' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    
    figures_generated = []
    
    # 1. Distribution plots
    for col in ['TotalPremium', 'TotalClaims']:
        if col in df.columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f"Distribution of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            filepath = os.path.join(FIGURES_DIR, f'dist_{col}.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")
    
    # 2. Boxplots for outlier detection
    for col in ['TotalPremium', 'TotalClaims']:
        if col in df.columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=df[col].dropna())
            plt.title(f"Boxplot of {col}")
            filepath = os.path.join(FIGURES_DIR, f'box_{col}.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")
    
    # 3. Scatter plot
    if 'TotalPremium' in df.columns and 'TotalClaims' in df.columns:
        plt.figure(figsize=(10, 6))
        valid_data = df.dropna(subset=['TotalPremium', 'TotalClaims'])
        sample_size = min(5000, len(valid_data))
        if sample_size > 0:
            sample = valid_data.sample(sample_size) if len(valid_data) > sample_size else valid_data
            sns.scatterplot(data=sample, x='TotalPremium', y='TotalClaims', alpha=0.5)
            plt.title("TotalPremium vs TotalClaims")
            filepath = os.path.join(FIGURES_DIR, 'scatter_TotalPremium_TotalClaims.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")
    
    # Alternative: If using insurance.csv structure (charges as premium proxy)
    if 'charges' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['charges'].dropna(), kde=True)
        plt.title("Distribution of Charges")
        filepath = os.path.join(FIGURES_DIR, 'dist_charges.png')
        plt.savefig(filepath, dpi=100, bbox_inches='tight')
        plt.close()
        figures_generated.append(filepath)
        print(f"   Generated: {filepath}")
        
        # Charges boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df['charges'].dropna())
        plt.title("Boxplot of Charges")
        filepath = os.path.join(FIGURES_DIR, 'box_charges.png')
        plt.savefig(filepath, dpi=100, bbox_inches='tight')
        plt.close()
        figures_generated.append(filepath)
        print(f"   Generated: {filepath}")
        
        # Charges by smoker
        if 'smoker' in df.columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=df, x='smoker', y='charges')
            plt.title("Charges by Smoker Status")
            filepath = os.path.join(FIGURES_DIR, 'box_charges_by_smoker.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")
        
        # Charges by region
        if 'region' in df.columns:
            plt.figure(figsize=(12, 6))
            sns.barplot(data=df, x='region', y='charges', estimator='mean')
            plt.title("Average Charges by Region")
            filepath = os.path.join(FIGURES_DIR, 'bar_charges_by_region.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")
        
        # Age vs Charges scatter
        if 'age' in df.columns:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x='age', y='charges', hue='smoker' if 'smoker' in df.columns else None, alpha=0.6)
            plt.title("Age vs Charges")
            filepath = os.path.join(FIGURES_DIR, 'scatter_age_charges.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")
        
        # BMI vs Charges
        if 'bmi' in df.columns:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x='bmi', y='charges', hue='smoker' if 'smoker' in df.columns else None, alpha=0.6)
            plt.title("BMI vs Charges")
            filepath = os.path.join(FIGURES_DIR, 'scatter_bmi_charges.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")

    
    # 4. Loss Ratio by categories
    if 'TotalPremium' in df.columns and 'TotalClaims' in df.columns:
        for cat_col in ['Province', 'VehicleType', 'Gender']:
            if cat_col in df.columns:
                group = df.groupby(cat_col)[['TotalPremium', 'TotalClaims']].sum()
                group['LossRatio'] = group['TotalClaims'] / group['TotalPremium']
                group = group.reset_index()
                
                plt.figure(figsize=(12, 6))
                sns.barplot(data=group, x=cat_col, y='LossRatio')
                plt.title(f'Loss Ratio by {cat_col}')
                plt.xticks(rotation=45, ha='right')
                filepath = os.path.join(FIGURES_DIR, f'bar_Loss_Ratio_by_{cat_col}.png')
                plt.savefig(filepath, dpi=100, bbox_inches='tight')
                plt.close()
                figures_generated.append(filepath)
                print(f"   Generated: {filepath}")
    
    # 5. Time series
    if 'TransactionMonth' in df.columns:
        monthly = df.groupby('TransactionMonth')[['TotalPremium', 'TotalClaims']].sum().reset_index()
        monthly = monthly.dropna().sort_values('TransactionMonth')
        
        if len(monthly) > 1:
            plt.figure(figsize=(14, 7))
            plt.plot(monthly['TransactionMonth'], monthly['TotalPremium'], label='TotalPremium')
            plt.plot(monthly['TransactionMonth'], monthly['TotalClaims'], label='TotalClaims')
            plt.title("Time Series Analysis")
            plt.legend()
            plt.xticks(rotation=45)
            filepath = os.path.join(FIGURES_DIR, 'time_series.png')
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            figures_generated.append(filepath)
            print(f"   Generated: {filepath}")
    
    # 6. Additional analysis plots
    # Premium distribution by Province
    if 'Province' in df.columns and 'TotalPremium' in df.columns:
        plt.figure(figsize=(12, 6))
        province_premium = df.groupby('Province')['TotalPremium'].sum().sort_values(ascending=False)
        province_premium.plot(kind='bar')
        plt.title('Total Premium by Province')
        plt.xlabel('Province')
        plt.ylabel('Total Premium')
        plt.xticks(rotation=45, ha='right')
        filepath = os.path.join(FIGURES_DIR, 'bar_Premium_by_Province.png')
        plt.savefig(filepath, dpi=100, bbox_inches='tight')
        plt.close()
        figures_generated.append(filepath)
        print(f"   Generated: {filepath}")
    
    print(f"\n   Total figures generated: {len(figures_generated)}")
    return figures_generated

def print_summary(df):
    """Print summary statistics of the integrated data."""
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    
    print(f"\nDataset Shape: {df.shape}")
    print(f"Total Records: {len(df):,}")
    
    if 'TotalPremium' in df.columns:
        print(f"\nTotalPremium:")
        print(f"   Sum: {df['TotalPremium'].sum():,.2f}")
        print(f"   Mean: {df['TotalPremium'].mean():,.2f}")
        print(f"   Median: {df['TotalPremium'].median():,.2f}")
    
    if 'TotalClaims' in df.columns:
        print(f"\nTotalClaims:")
        print(f"   Sum: {df['TotalClaims'].sum():,.2f}")
        print(f"   Mean: {df['TotalClaims'].mean():,.2f}")
        print(f"   Median: {df['TotalClaims'].median():,.2f}")
    
    if 'TotalPremium' in df.columns and 'TotalClaims' in df.columns:
        total_premium = df['TotalPremium'].sum()
        total_claims = df['TotalClaims'].sum()
        if total_premium > 0:
            loss_ratio = total_claims / total_premium
            print(f"\nOverall Loss Ratio: {loss_ratio:.2%}")

if __name__ == "__main__":
    # Load data
    df_insurance, df_claims = load_and_explore()
    
    # Integrate data
    df_integrated = integrate_data(df_insurance, df_claims)
    
    # Generate figures
    generate_figures(df_integrated)
    
    # Print summary
    print_summary(df_integrated)
    
    print("\n" + "=" * 60)
    print("DATA INTEGRATION COMPLETE!")
    print("=" * 60)
