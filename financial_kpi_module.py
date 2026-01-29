
import pandas as pd
import numpy as np

class FinancialKPICalculator:
    """
    Calculates financial KPIs for the dashboard.
    """
    
    def __init__(self):
        self.data = None
        self.processed_data = None
        
    def load_data(self, data_file):
        # Load csv and fix dates
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        return self.data
    
    def calculate_kpis(self):
        if self.data is None:
            raise ValueError("Load data first")
            
        df = self.data.copy()
        
        # Metric 1: Efficiency Score (0-100 scale based on errors)
        # Penalize 5 pts per error, 10 pts per compliance flag
        df['Efficiency_Score'] = 100 - (df['Settlement_Errors'] * 5) - (df['Compliance_Checks'] * 10)
        df['Efficiency_Score'] = df['Efficiency_Score'].clip(lower=0) 
        
        # Metric 2: Excess Return vs Risk Free Rate (0.01% daily assumption)
        rfr = 0.0001
        df['Excess_Return'] = df['Daily_Return'] - rfr
        
        # Metric 3: Performance Buckets
        conditions = [
            (df['Daily_Return'] > 0.01),
            (df['Daily_Return'] < -0.005)
        ]
        choices = ['High Performer', 'Underperformer']
        df['Performance_Category'] = np.select(conditions, choices, default='Neutral')
        
        self.processed_data = df
        return df
        
    def get_summary_report(self):
        # Aggregation for sanity check
        if self.processed_data is None:
            self.calculate_kpis()
            
            
        # Group by Asset Class and Date
        summary = self.processed_data.groupby(['Date', 'Asset_Class']).agg({
            'Market_Value': 'sum',
            'Daily_Return': 'mean',
            'Settlement_Errors': 'sum',
            'Efficiency_Score': 'mean'
        }).reset_index()
        
        return summary
    
    def export_to_sql_format(self, output_path):
        if self.processed_data is None:
            self.calculate_kpis()
            
        self.processed_data.to_csv(output_path, index=False)
        print(f"Exported to {output_path}")

